#!/usr/bin/env python3
"""
更新 README.md 的 star feed 区域

数据流：
  AI 输出结构化 JSON → 脚本渲染为 Markdown → 嵌入 README.md 的 FEED 区域

环境变量：
  AI_OUTPUT_FILE  - AI 生成结果的响应文件路径（由 actions/ai-inference@v1 提供）
  UPDATE_TIME     - 更新时间字符串（可选，默认用 AI 输出中的 date）

AI 输出 JSON 格式（由 workflow 中的 AI prompt 约定生成）：
{
  "date": "2026-06-25",
  "items": [
    {
      "repo": "owner/repo",
      "url": "https://github.com/owner/repo",
      "tag": "v1.2.3",
      "release_url": "https://github.com/owner/repo/releases/tag/v1.2.3",
      "release_date": "2026-06-25",
      "changes": ["更新内容1", "更新内容2"]
    }
  ]
}

用法：
  python scripts/update_readme.py                     # 正常更新（需要 AI_OUTPUT_FILE）
  python scripts/update_readme.py --validate          # 校验 AI JSON 格式
  python scripts/update_readme.py --dry-run           # 渲染但不写文件（需要 AI_OUTPUT_FILE）
"""
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
README_PATH = "README.md"

# ── AI 输出 JSON 结构校验 ──────────────────────────────────────────


def validate_item(item: dict) -> list[str]:
    """校验单个 item，返回错误列表"""
    errors = []
    if not isinstance(item.get("repo"), str) or not item["repo"]:
        errors.append("item.repo: 必须是非空字符串")
    if not isinstance(item.get("url"), str) or not item["url"]:
        errors.append("item.url: 必须是非空字符串")
    if not isinstance(item.get("release_date"), str) or not item["release_date"]:
        errors.append("item.release_date: 必须是非空字符串")
    if "tag" in item and not isinstance(item["tag"], str):
        errors.append("item.tag: 必须是字符串")
    if "changes" in item and not isinstance(item["changes"], list):
        errors.append("item.changes: 必须是数组")
    if "release_url" in item and not isinstance(item["release_url"], str):
        errors.append("item.release_url: 必须是字符串")
    return errors


def validate_feed(data: dict) -> list[str]:
    """校验整个 feed JSON，返回错误列表"""
    errors = []
    if not isinstance(data, dict):
        return ["根元素必须是 JSON 对象"]

    if "date" not in data or not isinstance(data.get("date"), str):
        errors.append("date: 必须存在且为字符串")
    if "items" not in data or not isinstance(data.get("items"), list):
        errors.append("items: 必须存在且为数组")
    else:
        for i, item in enumerate(data["items"]):
            item_errors = validate_item(item)
            for e in item_errors:
                errors.append(f"items[{i}].{e}")
    return errors

# ── Markdown 渲染 ──────────────────────────────────────────────────


def render_item(item: dict) -> str:
    """将单个 item 渲染为 Markdown 块"""
    repo = item["repo"]
    url = item["url"]
    release_url = item.get("release_url", url)
    release_date = item.get("release_date", "")
    tag = item.get("tag", "")
    changes = item.get("changes", [])

    lines = [f"- 📅 {release_date}"]

    # repo 行：加粗链接 + 可选 tag 标签
    repo_line = f"- **[{repo}]({url})**"
    if tag:
        repo_line += f" `{tag}`"
    lines.append(repo_line)

    # 更新内容
    if changes:
        lines.append("- 📝 更新内容：")
        for c in changes:
            lines.append(f"  - {c}")
    else:
        lines.append("- 📝 更新内容：项目常规更新维护")

    # release 链接
    lines.append(f"- 🔗 [查看 Release]({release_url})")

    return "\n".join(lines)


def render_feed(items: list) -> str:
    """将所有 items 渲染为完整的 FEED Markdown 内容"""
    if not items:
        return "📭 今日无更新"

    parts = [render_item(item) for item in items]
    return "\n\n---\n\n".join(parts)

# ── 主逻辑 ─────────────────────────────────────────────────────────


def read_ai_json(ai_output_file: str) -> dict | None:
    """读取并解析 AI 输出的 JSON 文件"""
    if not ai_output_file or not os.path.exists(ai_output_file):
        print("⚠️ AI 输出文件不存在或未指定")
        return None

    with open(ai_output_file, "r", encoding="utf-8") as f:
        raw = f.read().strip()

    if not raw:
        print("⚠️ AI 输出文件为空")
        return None

    # 去掉可能的 Markdown 代码块围栏
    raw = re.sub(r'^```(?:json)?\s*\n?', '', raw)
    raw = re.sub(r'\n?```\s*$', '', raw)
    raw = raw.strip()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"❌ AI 输出 JSON 解析失败: {e}")
        print(f"--- 原始内容前 200 字符 ---\n{raw[:200]}")
        return None

    return data


def find_feed_bounds(content: str) -> tuple[int, int] | None:
    """找到 FEED 区域起止位置，返回 (start_end_index, end_start_index)"""
    start_marker = "<!-- FEED -->"
    end_marker = "<!-- /FEED -->"

    start_idx = content.find(start_marker)
    if start_idx == -1:
        return None
    start_end = start_idx + len(start_marker)

    end_idx = content.find(end_marker)
    if end_idx == -1:
        return None
    end_start = end_idx

    return (start_end, end_start)


def update_timestamp(content: str, update_time: str) -> str:
    """更新时间戳行：**更新于 xxx**"""
    return re.sub(
        r'\*\*更新于[^*]*\*\*',
        f'**更新于 {update_time}**',
        content
    )


def main():
    dry_run = "--dry-run" in sys.argv
    validate_only = "--validate" in sys.argv

    ai_output_file = os.environ.get("AI_OUTPUT_FILE", "")

    # --validate 模式：校验 AI 输出但不写文件
    if validate_only:
        if not ai_output_file:
            print("❌ --validate 需要设置 AI_OUTPUT_FILE 环境变量")
            sys.exit(1)
        data = read_ai_json(ai_output_file)
        if data is None:
            sys.exit(1)
        errors = validate_feed(data)
        if errors:
            print("❌ 校验未通过：")
            for e in errors:
                print(f"  - {e}")
            sys.exit(1)
        print(f"✅ 校验通过：{len(data.get('items', []))} 条 item")
        return

    # 正常模式：读 AI 输出
    data = read_ai_json(ai_output_file)
    if data is None:
        print("⚠️ AI 未返回有效内容，跳过更新")
        return

    errors = validate_feed(data)
    if errors:
        print("❌ AI 输出校验未通过，跳过更新：")
        for e in errors:
            print(f"  - {e}")
        return

    items = data.get("items", [])
    items.sort(key=lambda x: x.get("release_date", ""), reverse=True)
    feed_date = data.get("date", "")
    print(f"📝 AI 内容：{len(items)} 条更新，日期 {feed_date}")

    # 渲染 Markdown
    feed_content = render_feed(items)
    print(f"📝 渲染后长度：{len(feed_content)} 字符")

    # 更新时间
    update_time = os.environ.get("UPDATE_TIME",
                                  data.get("update_time", feed_date))

    if dry_run:
        print(f"\n{'='*40}\nFEED 内容预览：\n{'='*40}")
        print(feed_content)
        print(f"{'='*40}")
        print(f"更新时间戳：{update_time}")
        return

    # 读 README
    if not os.path.exists(README_PATH):
        print(f"❌ 未找到 {README_PATH}")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 找 FEED 边界
    bounds = find_feed_bounds(content)
    if not bounds:
        print("❌ 未在 README.md 中找到 FEED 标记")
        return

    start_end, end_start = bounds

    # 构造新内容
    new_content = (
        content[:start_end].rstrip() +
        "\n" + feed_content + "\n" +
        content[end_start:]
    )

    # 更新时间戳
    new_content = update_timestamp(new_content, update_time)

    # 写回
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    if items:
        print(f"✅ README.md 已更新：{len(items)} 项")
    else:
        print("✅ README.md 已更新：今日无更新")


if __name__ == "__main__":
    main()

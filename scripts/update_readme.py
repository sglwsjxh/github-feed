#!/usr/bin/env python3
"""
更新 README.md 的 star feed 区域

AI 生成的内容直接替换 STAR_FEED_START 和 STAR_FEED_END 之间的区域
没有历史管理，没有日期标签，当天直接覆盖

环境变量：
  AI_OUTPUT_FILE  - AI 生成结果的响应文件路径（由 actions/ai-inference@v1 提供）
  UPDATE_TIME     - 更新时间字符串，如 "2026-06-25 19:00"
"""
import os
import re
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
README_PATH = "README.md"


def read_ai_output(ai_output_file: str) -> str:
    """读取 AI 输出，清理可能的包裹标记"""
    if not ai_output_file or not os.path.exists(ai_output_file):
        return ""

    with open(ai_output_file, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text or text == "*(AI 未返回内容)*":
        return ""

    # 去掉可能的 markdown 代码块围栏
    text = re.sub(r'^```(?:markdown)?\s*\n?', '', text)
    text = re.sub(r'\n?```\s*$', '', text)
    text = text.strip()

    # 去掉 AI 可能输出的 STAR_FEED 包裹（以防万一）
    text = re.sub(r'<!-- STAR_FEED_START -->\s*', '', text)
    text = re.sub(r'\s*<!-- STAR_FEED_END -->', '', text)
    text = text.strip()

    return text


def main():
    ai_output_file = os.environ.get("AI_OUTPUT_FILE", "")
    update_time = os.environ.get("UPDATE_TIME",
                                  datetime.now(CST).strftime("%Y-%m-%d %H:%M"))

    # 1. 读取 AI 输出
    ai_content = read_ai_output(ai_output_file)
    if not ai_content:
        print("⚠️ AI 未返回有效内容，跳过更新")
        return

    print(f"📝 AI 内容长度: {len(ai_content)} 字符")

    # 2. 读取 README
    if not os.path.exists(README_PATH):
        print(f"❌ 未找到 {README_PATH}")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 3. 更新时间戳
    content = re.sub(
        r'\*\*更新于[^*]*\*\*',
        f'**更新于 {update_time}**',
        content
    )

    # 4. 查找 STAR_FEED 区域，直接替换中间内容
    feed_match = re.search(
        r'<!-- STAR_FEED_START -->\n.*?\n<!-- STAR_FEED_END -->',
        content, re.DOTALL
    )

    if not feed_match:
        print("⚠️ 未找到 STAR_FEED_START/END 区域")
        return

    old_area = feed_match.group(0)
    new_area = f"<!-- STAR_FEED_START -->\n{ai_content}\n<!-- STAR_FEED_END -->"
    new_content = content.replace(old_area, new_area)

    # 5. 写回
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ README.md 已更新（直接覆盖）")


if __name__ == "__main__":
    main()

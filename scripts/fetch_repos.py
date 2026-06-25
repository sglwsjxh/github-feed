#!/usr/bin/env python3
"""
获取 GitHub starred 仓库列表及最新 release tag，输出 JSON 到 stdout

并发获取所有仓库的 latest release tag（最多 20 并发），
无 release 的仓库 tag 为空字符串。

用法：
  export GH_TOKEN=your_github_token
  python scripts/fetch_repos.py > starred_data.json
  python scripts/fetch_repos.py --dry-run   # 不调 API，输出格式示例

输出 JSON 格式：
{
  "count": 100,
  "date": "2026-06-25",
  "fetch_time": "2026-06-25 08:15",
  "repos": [
    { "name": "owner/repo",
      "description": "...",
      "url": "https://github.com/owner/repo",
      "lang": "Python",
      "stars": 100,
      "pushed": "2026-06-25 08:44",
      "release": {
        "tag": "v1.2.3",
        "published_at": "2026-06-25 00:44",
        "html_url": "https://github.com/owner/repo/releases/tag/v1.2.3",
        "body": "Release notes content..."
      }
    }
  ]
}
"""
import concurrent.futures
import json
import os
import subprocess
import sys
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
TAG_FETCH_WORKERS = 20


def main():
    if "--dry-run" in sys.argv:
        _show_dry_run()
        return

    gh_token = os.environ.get("GH_TOKEN", "")
    if not gh_token:
        _exit_error("GH_TOKEN 未设置")

    env = os.environ.copy()
    env["GH_TOKEN"] = gh_token

    try:
        result = subprocess.run(
            [
                "gh", "api", "/user/starred?per_page=100",
                "--jq", '[.[] | {name: .full_name, description: (.description // ""), url: .html_url, lang: (.language // ""), stars: .stargazers_count, pushed: .pushed_at}]'
            ],
            capture_output=True, text=True, check=True,
            env=env
        )
        repos = json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        _exit_error(f"gh api 调用失败: {e.stderr}")
    except json.JSONDecodeError:
        _exit_error("gh api 返回非 JSON")

    _fetch_tags(repos, env)
    for repo in repos:
        repo["pushed"] = _to_cst_str(repo["pushed"])

    # 预过滤：只保留近 7 天内有 release 发布的仓库
    # 在 Python 侧做过滤，不依赖 AI 理解日期条件
    cutoff = (datetime.now(CST) - timedelta(days=7)).strftime("%Y-%m-%d %H:%M")
    before = len(repos)
    repos = [r for r in repos
             if r.get("release") and r["release"].get("published_at")
             and r["release"]["published_at"] >= cutoff]
    dropped = before - len(repos)
    if dropped:
        print(f"  🗑️ 过滤掉 {dropped} 个超过 7 天的 release", file=sys.stderr)

    now = datetime.now(CST)
    output = {
        "count": len(repos),
        "date": now.strftime("%Y-%m-%d"),
        "fetch_time": now.strftime("%Y-%m-%d %H:%M"),
        "repos": repos
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


RELEASE_BODY_MAX = 500


def _get_latest_release(repo_name: str, env: dict) -> dict | None:
    try:
        result = subprocess.run(
            [
                "gh", "api", f"repos/{repo_name}/releases/latest",
                "--jq", '{tag: .tag_name, published_at: .published_at, html_url: .html_url, body: .body}'
            ],
            capture_output=True, text=True, check=True,
            env=env
        )
        release = json.loads(result.stdout)
        if release.get("published_at"):
            release["published_at"] = _to_cst_str(release["published_at"])
        if release.get("body"):
            release["body"] = release["body"][:RELEASE_BODY_MAX]
        return release
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return None


def _fetch_tags(repos: list, env: dict):
    total = len(repos)
    print(f"🔍 获取 {total} 个仓库的 release 信息...", file=sys.stderr)

    with concurrent.futures.ThreadPoolExecutor(max_workers=TAG_FETCH_WORKERS) as executor:
        future_to_repo = {
            executor.submit(_get_latest_release, repo["name"], env): repo
            for repo in repos
        }
        done = 0
        for future in concurrent.futures.as_completed(future_to_repo):
            repo = future_to_repo[future]
            repo["release"] = future.result()
            done += 1
            if done % 10 == 0 or done == total:
                print(f"  ⏳ {done}/{total}", file=sys.stderr)

    tagged = sum(1 for r in repos if r.get("release"))
    print(f"✅ 完成：{tagged}/{total} 个仓库有 release", file=sys.stderr)


def _to_cst_str(iso_str: str) -> str:
    if not iso_str:
        return ""
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.astimezone(CST).strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return iso_str[:10]


def _exit_error(msg: str):
    print(json.dumps({"error": msg, "count": 0, "date": "", "fetch_time": "", "repos": []}))
    sys.exit(1)


def _show_dry_run():
    example = {
        "count": 2,
        "date": "2026-06-25",
        "fetch_time": "2026-06-25 08:15",
        "repos": [
            {
                "name": "owner/repo-a",
                "description": "示例仓库 A",
                "url": "https://github.com/owner/repo-a",
                "lang": "Python",
                "stars": 100,
                "pushed": "2026-06-25 08:44",
                "release": {
                    "tag": "v2.0.0",
                    "published_at": "2026-06-25 00:44",
                    "html_url": "https://github.com/owner/repo-a/releases/tag/v2.0.0",
                    "body": "## What's New\n- Feature A released\n- Bug fixes"
                }
            },
            {
                "name": "owner/repo-b",
                "description": "示例仓库 B",
                "url": "https://github.com/owner/repo-b",
                "lang": "TypeScript",
                "stars": 200,
                "pushed": "2026-06-24 20:00",
                "release": None
            }
        ]
    }
    print(json.dumps(example, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
获取 GitHub starred 仓库列表，输出 JSON 到 stdout

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
      "pushed": "2026-06-25T00:00:00Z" }
  ]
}
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))


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

    now = datetime.now(CST)
    output = {
        "count": len(repos),
        "date": now.strftime("%Y-%m-%d"),
        "fetch_time": now.strftime("%Y-%m-%d %H:%M"),
        "repos": repos
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def _exit_error(msg: str):
    print(json.dumps({"error": msg, "count": 0, "date": "", "fetch_time": "", "repos": []}))
    sys.exit(1)


def _show_dry_run():
    """展示输出格式示例，方便 workflow 调试"""
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
                "pushed": "2026-06-25T00:00:00Z"
            },
            {
                "name": "owner/repo-b",
                "description": "示例仓库 B",
                "url": "https://github.com/owner/repo-b",
                "lang": "TypeScript",
                "stars": 200,
                "pushed": "2026-06-24T12:00:00Z"
            }
        ]
    }
    print(json.dumps(example, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

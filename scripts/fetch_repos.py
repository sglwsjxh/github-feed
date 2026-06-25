#!/usr/bin/env python3
"""
获取 GitHub starred 仓库列表，输出 JSON 到 stdout
调用 gh api 获取数据，提取关键字段

用法：
  export GH_TOKEN=your_github_token
  python scripts/fetch_repos.py > starred_data.json

输出 JSON 格式：
{
  "count": 100,
  "date": "2026-06-25",
  "update_time": "2026-06-25 19:00",
  "repos": [
    { "name": "owner/repo", "description": "...", "url": "...",
      "lang": "Python", "stars": 100, "pushed": "2026-06-25T10:00:00Z" }
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
    gh_token = os.environ.get("GH_TOKEN", "")
    if not gh_token:
        print(json.dumps({"error": "GH_TOKEN 未设置", "count": 0, "date": "", "update_time": "", "repos": []}))
        sys.exit(1)

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
        print(json.dumps({"error": f"gh api 调用失败: {e.stderr}", "count": 0, "date": "", "update_time": "", "repos": []}))
        sys.exit(1)
    except json.JSONDecodeError:
        print(json.dumps({"error": "gh api 返回非 JSON", "count": 0, "date": "", "update_time": "", "repos": []}))
        sys.exit(1)

    now = datetime.now(CST)
    today = now.strftime("%Y-%m-%d")
    update_time = now.strftime("%Y-%m-%d %H:%M")

    output = {
        "count": len(repos),
        "date": today,
        "update_time": update_time,
        "repos": repos
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

"""
Generate a Hugo blog article about tech trends using Google Gemini API.

This script calls the Gemini API to generate an article about technology trends
and development techniques, then saves it as a properly formatted Hugo Markdown file
with the 'ai' tag.

Usage:
    python scripts/generate_article.py

Environment Variables:
    GEMINI_API_KEY: Google Gemini API key (required)
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta


def call_gemini_api(api_key: str, prompt: str) -> str:
    """Call Google Gemini API and return the generated text."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.9,
            "topP": 0.95,
            "maxOutputTokens": 4096,
        },
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"Gemini API HTTP Error {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Gemini API URL Error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    try:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError) as e:
        print(f"Unexpected API response structure: {e}", file=sys.stderr)
        print(f"Response: {json.dumps(result, indent=2)}", file=sys.stderr)
        sys.exit(1)

    return text


def build_prompt() -> str:
    """Build the prompt for Gemini to generate a tech article in Traditional Chinese."""
    return """你是一位資深的科技部落格作家，擅長撰寫繁體中文的技術文章。

請撰寫一篇關於「科技趨勢與開發技術」的文章，主題可以從以下方向中選擇一個或多個來深入探討：
- AI / 機器學習的最新應用與開發實踐
- 雲端原生技術 (Cloud Native) 的發展
- DevOps / CI/CD 的最佳實踐
- 新興程式語言或框架的趨勢
- 資安與隱私保護的新挑戰
- 邊緣運算 (Edge Computing) 的應用場景
- 開源社群的最新動態

文章要求：
1. 使用繁體中文撰寫
2. 文章需有清楚的架構，包含前言、主要內容段落、結論
3. 使用 Markdown 格式的標題 (## 二級標題, ### 三級標題)
4. 適當加入程式碼範例（如果適用的話）
5. 文章長度約 800-1500 字
6. 語調專業但親切，適合開發者閱讀
7. 不要包含 front matter（即不要包含 --- 開頭的 YAML 區塊），直接從文章的第一個標題開始

請直接輸出文章內容，不要加入任何額外的說明或包裝。"""


def extract_title_and_slug(article_content: str) -> tuple[str, str]:
    """Extract title from the first heading of the article and generate a slug."""
    lines = article_content.strip().split("\n")
    title = "科技趨勢與開發技術"
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            # Remove all leading '#' and spaces
            title = stripped.lstrip("#").strip()
            break

    # Generate a simple slug from the date
    slug = f"ai-tech-trends-{datetime.now().strftime('%Y%m%d')}"
    return title, slug


def build_front_matter(title: str, slug: str, now: datetime) -> str:
    """Build Hugo front matter in YAML format."""
    date_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")
    front_matter = f"""---
title: "{title}"
description: "由 AI 自動生成的科技趨勢與開發技術文章"
date: {date_str}
slug: "{slug}"
categories:
    - Experience
tags:
    - ai
math: false
license: CC BY-NC-SA 4.0
hidden: false
comments: true
draft: false
---"""
    return front_matter


def clean_article_content(content: str) -> str:
    """Clean up the article content, removing any accidental front matter."""
    content = content.strip()

    # Remove wrapping markdown code fences if present
    if content.startswith("```markdown"):
        content = content[len("```markdown"):].strip()
    elif content.startswith("```md"):
        content = content[len("```md"):].strip()
    elif content.startswith("```"):
        content = content[3:].strip()

    if content.endswith("```"):
        content = content[:-3].strip()

    # Remove front matter block if Gemini accidentally added one
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].strip()

    return content


def main():
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    print("Generating article using Gemini API...")
    prompt = build_prompt()
    raw_content = call_gemini_api(api_key, prompt)
    article_content = clean_article_content(raw_content)

    # Use UTC+8 (Taiwan timezone)
    tz = timezone(timedelta(hours=8))
    now = datetime.now(tz)

    title, slug = extract_title_and_slug(article_content)
    front_matter = build_front_matter(title, slug, now)

    full_content = f"{front_matter}\n\n{article_content}\n"

    # Determine output path
    output_dir = os.path.join("content", "posts", "ai")
    os.makedirs(output_dir, exist_ok=True)

    filename = f"{now.strftime('%Y%m%d')}_{slug}.md"
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_content)

    print(f"Article generated successfully: {output_path}")
    print(f"Title: {title}")

    # Output for GitHub Actions
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"article_path={output_path}\n")
            f.write(f"article_title={title}\n")


if __name__ == "__main__":
    main()

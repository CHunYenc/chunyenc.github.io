"""
Generate a Hugo blog article using Google Gemini API.

This script calls the Gemini API to generate a deep-dive technical article
focused on developer growth, engineering mindset, and practical wisdom.
The article is saved as a properly formatted Hugo Markdown file with the 'ai' tag.

Usage:
    python scripts/generate_article.py

Environment Variables:
    GEMINI_API_KEY: Google Gemini API key (required)
"""

import os
import sys
import json
import random
import hashlib
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta


# ---------------------------------------------------------------------------
# Topic definitions — each topic is a structured prompt blueprint
# ---------------------------------------------------------------------------

TOPICS = [
    {
        "id": "junior-to-senior",
        "role": "你是一位資深的技術主管（Engineering Manager）兼技術布道師。你見過無數工程師的成長，深諳 Junior 與 Senior 之間那道「隱形牆」在哪裡。你的文字風格冷靜、精闢，能一針見血地指出開發者的思維誤區。",
        "task": "撰寫一篇深度技術專題文章，主題為「從 Junior 到 Senior：開發者必須完成的思維與技術轉型」。",
        "dimensions": [
            "**從「實作功能」到「設計系統」**：討論過度設計（Over-engineering）與設計不足的取捨。",
            "**從「修復 Bug」到「管理複雜度」**：探討程式碼的可維護性、單元測試與技術債的平衡。",
            "**從「個人貢獻」到「技術影響力」**：如何進行有效的 Code Review 與技術決策。",
        ],
        "audience": "工作 2-3 年、處於瓶頸期的 Junior/Mid-level 工程師。他們渴望知道除了寫好程式碼之外，還需要具備哪些「資深感」的特質。",
        "constraints": [
            "必須包含一個關於「重構」或「架構抉擇」的具體情境分析（例如：為什麼不應該盲目追求微服務）。",
            "提供兩段程式碼對比：Junior 版（直覺但難以擴充的寫法）vs Senior 版（考慮了抽象化、依賴注入或錯誤處理的健壯寫法）。",
        ],
        "core_message": "資深工程師看重的是商業價值與系統穩定，而不僅是新技術。",
    },
    {
        "id": "debugging-mindset",
        "role": "你是一位在大型分散式系統中歷經無數次生產環境事故的 Staff Engineer。你擅長用清晰的因果鏈拆解複雜問題，文字風格沉穩、有說服力。",
        "task": "撰寫一篇深度技術專題文章，主題為「除錯的藝術：從盲目 print 到系統性問題分析」。",
        "dimensions": [
            "**問題定位的思維框架**：二分法、假設驅動、最小可重現案例。",
            "**Observability 三本柱**：Logging、Metrics、Tracing 在實戰中如何搭配使用。",
            "**生產環境除錯的紀律**：如何在壓力下保持冷靜，避免「修東牆補西牆」。",
        ],
        "audience": "開發 1-3 年、遇到複雜 Bug 時容易慌張或毫無方向感的工程師。",
        "constraints": [
            "必須包含一個實際的除錯情境：例如一個 API 間歇性超時的根因分析流程。",
            "提供兩段程式碼對比：缺乏錯誤處理的 Junior 版 vs 有完整 logging 與 graceful degradation 的 Senior 版。",
        ],
        "core_message": "除錯能力不是天賦，而是一套可以被訓練的系統性思維。",
    },
    {
        "id": "api-design-philosophy",
        "role": "你是一位 API 設計領域的專家，曾主導多個公開 API 平台的設計。你對向後相容性（backward compatibility）有近乎偏執的堅持，文字風格嚴謹且富有洞見。",
        "task": "撰寫一篇深度技術專題文章，主題為「好的 API 是一份契約：從介面設計看工程師的成熟度」。",
        "dimensions": [
            "**命名與一致性**：為什麼 API 的命名規範比你想的更重要。",
            "**錯誤處理設計**：HTTP status code 的正確使用、錯誤回應的結構化設計。",
            "**版本策略與向後相容**：如何在不破壞既有使用者的前提下迭代 API。",
        ],
        "audience": "已經能寫出 CRUD API 但不理解「為什麼我的 API 總是被抱怨難用」的工程師。",
        "constraints": [
            "必須包含一個關於 API 版本遷移或 breaking change 的具體情境分析。",
            "提供兩段 API endpoint 設計對比：不一致且缺乏錯誤處理的 Junior 版 vs 結構清晰、考慮邊界情況的 Senior 版。",
        ],
        "core_message": "API 設計的品質直接反映了工程師是否真正站在使用者（呼叫端）的角度思考。",
    },
    {
        "id": "technical-debt",
        "role": "你是一位歷經多次大型系統重寫的架構師。你對技術債有深刻的理解——你知道什麼時候該忍耐它、什麼時候該償還它。你的文字風格務實、不教條。",
        "task": "撰寫一篇深度技術專題文章，主題為「技術債不是髒話：務實工程師的債務管理策略」。",
        "dimensions": [
            "**技術債的分類**：刻意的 vs 無意的、短期的 vs 長期的。",
            "**量化與溝通**：如何向非技術主管解釋技術債的成本與風險。",
            "**償還策略**：Boy Scout Rule、策略性重構、以及「大爆炸重寫」為何通常是陷阱。",
        ],
        "audience": "覺得「程式碼好髒但沒人讓我重構」的中階工程師，以及不確定該如何安排重構優先級的 Tech Lead。",
        "constraints": [
            "必須包含一個「大爆炸重寫 vs 漸進式重構」的具體情境比較與結論。",
            "提供兩段程式碼對比：技術債累積後難以修改的版本 vs 套用策略性重構後清晰可維護的版本。",
        ],
        "core_message": "成熟的工程師不會追求零技術債，而是有意識地管理它，把重構當作持續的投資而非一次性的革命。",
    },
    {
        "id": "testing-philosophy",
        "role": "你是一位對軟體品質有極高要求的資深工程師。你推崇務實的測試策略，反對為了覆蓋率而寫測試的形式主義。文字風格直接、不迂迴。",
        "task": "撰寫一篇深度技術專題文章，主題為「測試的真諦：為什麼你的 100% 覆蓋率毫無意義」。",
        "dimensions": [
            "**測試金字塔的實戰應用**：Unit、Integration、E2E 各層的投資比例與取捨。",
            "**什麼值得測試**：商業邏輯的邊界條件 vs 膠水程式碼（glue code）的測試價值。",
            "**測試即文件**：好的測試如何成為系統行為的活文件（living documentation）。",
        ],
        "audience": "知道要寫測試但不確定「該測什麼」和「測到什麼程度」的工程師。",
        "constraints": [
            "必須包含一個「過度測試導致重構困難」或「關鍵路徑缺乏測試導致線上事故」的具體案例。",
            "提供兩段測試程式碼對比：測試實作細節的脆弱測試 vs 測試行為與契約的穩健測試。",
        ],
        "core_message": "測試的價值不在數量，而在於它是否真正守護了系統最重要的商業邏輯。",
    },
    {
        "id": "devops-culture",
        "role": "你是一位 DevOps 文化的推動者，在多家公司導入過 CI/CD 流程。你深知 DevOps 不只是工具，更是一種組織文化的轉型。文字風格平實但有力。",
        "task": "撰寫一篇深度技術專題文章，主題為「DevOps 不是一個職位：從 CI/CD Pipeline 到工程文化的全面升級」。",
        "dimensions": [
            "**CI/CD 的真正價值**：不只是自動化部署，而是快速回饋迴圈（feedback loop）。",
            "**Infrastructure as Code**：為什麼你的環境設定應該被版本控制。",
            "**On-call 文化與事後檢討（Postmortem）**：從事故中學習而非指責。",
        ],
        "audience": "仍然把 DevOps 理解為「會用 Docker 和 Jenkins」的工程師。",
        "constraints": [
            "必須包含一個具體的 CI/CD pipeline 設計範例或部署策略（如 Blue-Green、Canary）的情境分析。",
            "提供兩段對比：手動部署流程的痛點 vs 自動化 pipeline 的效益（可用流程圖或 YAML 片段）。",
        ],
        "core_message": "DevOps 的核心是縮短從程式碼提交到使用者價值交付的距離，工具只是手段。",
    },
    {
        "id": "clean-architecture",
        "role": "你是一位崇尚簡潔設計的軟體架構師。你相信好的架構不是看起來厲害，而是讓團隊能快速且安全地迭代。你的文字冷靜但充滿實戰智慧。",
        "task": "撰寫一篇深度技術專題文章，主題為「架構不是畫圖：從 Clean Architecture 到務實的分層設計」。",
        "dimensions": [
            "**依賴反轉原則（DIP）的真正意義**：不是為了抽象而抽象。",
            "**分層設計的取捨**：什麼時候 3 層架構就夠了，什麼時候需要 Hexagonal Architecture。",
            "**架構決策紀錄（ADR）**：為什麼「為什麼這樣設計」比「怎麼設計」更重要。",
        ],
        "audience": "讀過 Clean Architecture 書但覺得「在實際專案中用不上」的工程師。",
        "constraints": [
            "必須包含一個「過度分層導致開發效率下降」vs「適度分層帶來長期收益」的具體對比情境。",
            "提供兩段程式碼對比：業務邏輯與基礎設施高度耦合的版本 vs 清晰分離關注點的版本。",
        ],
        "core_message": "架構的目的是服務業務需求，而非滿足工程師對完美的追求。",
    },
    {
        "id": "code-review-culture",
        "role": "你是一位重視團隊協作的 Engineering Lead。你認為 Code Review 是提升團隊戰力最被低估的武器。你的文字風格溫暖但精準。",
        "task": "撰寫一篇深度技術專題文章，主題為「Code Review 的藝術：從找 Bug 到塑造團隊工程文化」。",
        "dimensions": [
            "**Review 的層次**：正確性、可讀性、架構一致性、知識傳遞。",
            "**如何給出有建設性的回饋**：避免情緒化批評，聚焦在「為什麼」而非「你錯了」。",
            "**被 Review 的心態**：如何接受回饋、如何從 Review 中加速成長。",
        ],
        "audience": "覺得 Code Review 只是形式、或者不知道該在 Review 中看什麼的工程師。",
        "constraints": [
            "必須包含一個具體的 Code Review 情境：展示一段 PR diff，以及好的 review comment vs 差的 review comment 的對比。",
            "提供兩段對比：一段只看語法問題的表層 review vs 一段觸及設計本質的深層 review。",
        ],
        "core_message": "Code Review 不只是品質門檻，更是團隊成員互相學習、對齊架構認知的最佳場域。",
    },
    {
        "id": "database-design",
        "role": "你是一位在高流量系統中處理過各種資料庫效能問題的後端資深工程師。你對 SQL 調優和資料模型設計有豐富的實戰經驗。文字風格務實、步驟清晰。",
        "task": "撰寫一篇深度技術專題文章，主題為「你的查詢為什麼這麼慢？從資料庫設計看後端工程師的基本功」。",
        "dimensions": [
            "**索引不是萬靈丹**：理解 B-Tree、covering index，以及過多索引的副作用。",
            "**正規化 vs 反正規化**：什麼時候該為了效能犧牲正規化。",
            "**N+1 問題與批次查詢**：ORM 使用者最常踩的坑。",
        ],
        "audience": "能寫出 CRUD 但遇到效能問題時只會「加個索引試試」的後端工程師。",
        "constraints": [
            "必須包含一個 SQL 查詢效能分析的具體情境（例如使用 EXPLAIN 分析）。",
            "提供兩段程式碼對比：產生 N+1 查詢的 ORM 寫法 vs 使用 eager loading 或 raw SQL 優化後的版本。",
        ],
        "core_message": "資料庫不是黑盒子，理解你的查詢在底層如何執行，是後端工程師從 Junior 晉升的關鍵門檻。",
    },
    {
        "id": "security-mindset",
        "role": "你是一位同時具備開發與資安背景的 Security Champion。你相信安全不是事後補救，而是在設計階段就該內建的思維。文字直接、不危言聳聽但態度嚴肅。",
        "task": "撰寫一篇深度技術專題文章，主題為「不要等到被打才學資安：開發者必備的安全思維」。",
        "dimensions": [
            "**OWASP Top 10 不只是考題**：Injection、XSS、CSRF 在現代框架中仍然存在的變體。",
            "**認證與授權的正確實作**：JWT 的常見誤用、OAuth 2.0 的陷阱。",
            "**Shift Left Security**：如何在 CI/CD 中嵌入安全檢查。",
        ],
        "audience": "認為「我又不是做資安的，這不關我的事」的一般開發者。",
        "constraints": [
            "必須包含一個具體的漏洞情境分析（例如一個看似正常但有 SQL Injection 風險的程式碼）。",
            "提供兩段程式碼對比：存在安全漏洞的版本 vs 套用安全最佳實踐的版本。",
        ],
        "core_message": "每一行你寫的程式碼都是攻擊面的一部分，安全思維應該像寫測試一樣成為開發者的基本素養。",
    },
]


def call_gemini_api(api_key: str, prompt: str) -> str:
    """Call Google Gemini API and return the generated text."""
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-2.0-flash:generateContent"
        f"?key={api_key}"
    )

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.85,
            "topP": 0.95,
            "maxOutputTokens": 8192,
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


def pick_topic(now: datetime) -> dict:
    """Pick a topic based on the current date for deterministic-but-rotating selection.

    Uses a hash of the date string to select a topic, ensuring the same date
    always produces the same topic, but different dates rotate through topics.
    """
    date_seed = now.strftime("%Y-%m-%d")
    hash_val = int(hashlib.md5(date_seed.encode()).hexdigest(), 16)
    return TOPICS[hash_val % len(TOPICS)]


def build_prompt(topic: dict) -> str:
    """Build a structured prompt from a topic definition."""
    dimensions_text = "\n".join(f"  {i+1}. {d}" for i, d in enumerate(topic["dimensions"]))
    constraints_text = "\n".join(f"  - {c}" for c in topic["constraints"])

    return f"""### 角色
{topic["role"]}

### 任務
{topic["task"]}
文章需涵蓋以下核心維度：
{dimensions_text}

### 情境
讀者是{topic["audience"]}

### 限制條件
- **核心論點**：{constraints_text}
- **語言風格**：台灣繁體中文，專業用語需精準（如：耦合度、抽象化、解耦、擴充性）。
- **字數要求**：1,500 字左右，內容需紮實，不要灌水。
- **格式要求**：使用 Markdown 分級標題，直接以 # 一級標題開始。不要包含 front matter（即不要包含 --- 開頭的 YAML 區塊）。
- **程式碼語言**：程式碼範例請使用 Python 或 JavaScript/TypeScript（選擇最適合該主題的語言）。

### 核心理念
文章必須成功傳達：「{topic["core_message"]}」

### 評估標準
- 是否成功傳達核心理念，而非流於泛泛的教科書敘述。
- 程式碼對比是否具有說服力，能體現出工程品質的差異。
- 是否有具體的情境分析，讓讀者能代入自身經驗產生共鳴。

請直接輸出文章內容，不要加入任何額外的說明、包裝或前言寒暄。"""


def extract_title_and_slug(article_content: str, topic_id: str) -> tuple[str, str]:
    """Extract title from the first heading of the article and generate a slug."""
    lines = article_content.strip().split("\n")
    title = "開發者成長筆記"
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            break

    slug = f"ai-{topic_id}-{datetime.now().strftime('%Y%m%d')}"
    return title, slug


def build_front_matter(title: str, slug: str, now: datetime, topic: dict) -> str:
    """Build Hugo front matter in YAML format."""
    date_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")
    return f"""---
title: "{title}"
description: "由 AI 生成的深度技術專題 — {topic['core_message']}"
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


def clean_article_content(content: str) -> str:
    """Clean up the article content, removing any accidental front matter or fences."""
    content = content.strip()

    # Remove wrapping markdown code fences if present
    for prefix in ("```markdown", "```md", "```"):
        if content.startswith(prefix):
            content = content[len(prefix):].strip()
            break

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

    # Use UTC+8 (Taiwan timezone)
    tz = timezone(timedelta(hours=8))
    now = datetime.now(tz)

    # Pick a topic for today
    topic = pick_topic(now)
    print(f"Selected topic: {topic['id']}")
    print(f"Core message: {topic['core_message']}")

    # Generate article
    print("Generating article using Gemini API...")
    prompt = build_prompt(topic)
    raw_content = call_gemini_api(api_key, prompt)
    article_content = clean_article_content(raw_content)

    title, slug = extract_title_and_slug(article_content, topic["id"])
    front_matter = build_front_matter(title, slug, now, topic)

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

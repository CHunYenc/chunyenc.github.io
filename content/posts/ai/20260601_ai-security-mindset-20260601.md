---
title: "不要等到被打才學資安：開發者必備的安全思維"
description: "由 AI 生成的深度技術專題 — 每一行你寫的程式碼都是攻擊面的一部分，安全思維應該像寫測試一樣成為開發者的基本素養。"
date: 2026-06-01T18:49:12+08:00
slug: "ai-security-mindset-20260601"
categories:
    - Experience
tags:
    - ai
math: false
license: CC BY-NC-SA 4.0
hidden: false
comments: true
draft: false
---

# 不要等到被打才學資安：開發者必備的安全思維

身為開發者，你可能覺得資安是資安團隊的事，跟你沒太大關係。但讓我直接了當地說：這種想法很危險。每一行你寫的程式碼都是攻擊面的一部分，安全思維應該像寫測試一樣成為開發者的基本素養。別再把資安當成事後補救，而是在設計階段就該內建的思維。

## OWASP Top 10 不只是考題：現代框架下的變體

OWASP Top 10 不是考題，而是真實世界的威脅。即使你用了現代框架，這些漏洞仍然可能以你意想不到的形式存在。

### Injection：SQL Injection 的現代變形

SQL Injection 並沒有消失，只是換了個樣子。ORM (Object-Relational Mapping) 並不能完全避免 SQL Injection，錯誤的使用方式仍然會導致漏洞。

**漏洞情境：看似正常的搜尋功能**

假設你有一個搜尋使用者名稱的功能，使用 ORM 如下：

```python
# 存在 SQL Injection 風險的版本
def search_user(username):
  query = f"SELECT * FROM users WHERE username LIKE '%{username}%'"
  result = db.execute(query)
  return result
```

乍看之下沒什麼問題，但如果 `username` 包含惡意字元，例如 `'; DROP TABLE users; --`，就會變成：

```sql
SELECT * FROM users WHERE username LIKE '%; DROP TABLE users; --%'
```

這段 SQL 會先選取所有使用者，然後刪除 `users` 表格，最後註解掉後面的部分。

**安全版本：使用參數化查詢**

```python
# 安全版本：使用參數化查詢
def search_user(username):
  query = "SELECT * FROM users WHERE username LIKE %s"
  params = (f"%{username}%",)
  result = db.execute(query, params)
  return result
```

使用參數化查詢，`username` 會被當作資料，而不是 SQL 指令的一部分，從而避免 SQL Injection。ORM 框架通常提供參數化查詢的功能，務必善用。

### XSS：不只是 `<script>` 標籤

Cross-Site Scripting (XSS) 不只是 `<script>` 標籤。現代框架雖然提供了預設的防護機制，但仍然需要小心處理使用者輸入。

例如，在 React 中，直接使用 `dangerouslySetInnerHTML` 就可能引入 XSS 漏洞。

### CSRF：狀態變更請求的保護

Cross-Site Request Forgery (CSRF) 攻擊利用使用者已登入的狀態，偽造請求執行惡意操作。現代框架通常提供 CSRF 防護機制，例如同步器令牌模式 (Synchronizer Token Pattern)，但需要正確啟用和配置。

## 認證與授權的正確實作：JWT 與 OAuth 2.0 的陷阱

認證 (Authentication) 確認使用者是誰，授權 (Authorization) 決定使用者可以做什麼。這兩個環節的實作稍有不慎，就會造成嚴重的安全漏洞。

### JWT 的常見誤用

JSON Web Token (JWT) 是一種常見的認證方式，但使用不當可能會導致安全問題。

*   **不要把敏感資訊放在 JWT 的 payload 中**：JWT 是可以被解碼的，雖然無法竄改（如果簽章正確），但任何人都可以讀取 payload 中的內容。
*   **驗證簽章是必須的**：沒有驗證簽章的 JWT 等於沒有保護。
*   **使用安全的金鑰管理**：金鑰洩漏會導致嚴重的安全問題。

### OAuth 2.0 的陷阱

OAuth 2.0 是一種授權框架，允許第三方應用程式代表使用者存取資源。

*   **正確驗證 `redirect_uri`**：攻擊者可以利用未經驗證的 `redirect_uri` 竊取授權碼。
*   **使用 PKCE (Proof Key for Code Exchange)**：PKCE 可以防止授權碼被攔截。
*   **了解不同的 Grant Types 的安全風險**：例如，Implicit Grant Type 已經被棄用，因為它存在安全風險。

## Shift Left Security：在 CI/CD 中嵌入安全檢查

Shift Left Security 指的是將安全檢查提前到開發流程的早期階段，而不是等到部署之後才進行。

**如何在 CI/CD 中嵌入安全檢查？**

*   **靜態程式碼分析 (Static Application Security Testing, SAST)**：在程式碼提交時，自動掃描程式碼中的安全漏洞。
*   **軟體成分分析 (Software Composition Analysis, SCA)**：檢查專案依賴的第三方函式庫是否存在已知的安全漏洞。
*   **滲透測試 (Penetration Testing)**：定期進行滲透測試，模擬真實世界的攻擊，找出系統中的安全漏洞。
*   **自動化安全測試**：將安全測試納入自動化測試流程中，確保每次程式碼變更都經過安全檢查。

**範例：使用 GitHub Actions 進行 SAST**

```yaml
name: Security Scan

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run SAST
        uses: sonarsource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

這段 YAML 程式碼定義了一個 GitHub Actions 工作流程，在每次程式碼提交或 Pull Request 時，使用 SonarQube 進行靜態程式碼分析。

## 結論：安全是每個開發者的責任

安全不是資安團隊的專利，而是每個開發者的責任。不要再抱持著「這不關我的事」的想法，從現在開始，將安全思維融入你的開發流程中。學習 OWASP Top 10，了解常見的安全漏洞，並在程式碼中實踐安全最佳實踐。記住，安全不是事後補救，而是在設計階段就該內建的思維。只有這樣，我們才能建立更安全、更可靠的軟體系統。

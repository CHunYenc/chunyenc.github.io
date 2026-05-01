---
title: "Code Review 的藝術：從找 Bug 到塑造團隊工程文化"
description: "由 AI 生成的深度技術專題 — Code Review 不只是品質門檻，更是團隊成員互相學習、對齊架構認知的最佳場域。"
date: 2026-05-01T17:37:50+08:00
slug: "ai-code-review-culture-20260501"
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

# Code Review 的藝術：從找 Bug 到塑造團隊工程文化

各位夥伴，大家好！身為 Engineering Lead，我一直深信 Code Review 是提升團隊戰力最被低估的武器。它不只是抓 Bug 的工具，更是知識傳遞、架構對齊、塑造團隊工程文化的絕佳場域。今天，我想跟大家聊聊 Code Review 的藝術，希望能幫助大家更有效地運用這個強大的工具。

## Review 的層次：不只是語法檢查

很多人覺得 Code Review 就是檢查有沒有拼錯字、有沒有違反 coding style。當然，這些很重要，但 Code Review 的價值遠不止於此。我認為 Review 可以分為以下幾個層次：

1.  **正確性 (Correctness)**：這是最基本的要求。程式碼是否能正確地實現需求？有沒有邊界條件沒考慮到？有沒有潛在的錯誤處理問題？
2.  **可讀性 (Readability)**：程式碼是否易於理解？命名是否清晰？邏輯是否簡潔？好的程式碼應該像一篇優美的文章，讓人一看就懂。
3.  **架構一致性 (Architectural Consistency)**：程式碼是否符合團隊的架構規範？是否使用了正確的設計模式？是否與現有系統良好整合？
4.  **知識傳遞 (Knowledge Transfer)**：Reviewer 是否能從程式碼中學到新的知識？Author 是否能從 Reviewer 的回饋中獲得成長？這是 Code Review 最重要的價值之一。

## 如何給出有建設性的回饋：聚焦「為什麼」

給出有建設性的回饋，是 Code Review 的核心。以下是一些建議：

*   **避免情緒化批評**：不要說「這段程式碼寫得太爛了」，而要說「這段程式碼的邏輯有點複雜，可以考慮用更簡潔的方式實現」。
*   **聚焦在「為什麼」而非「你錯了」**：不要直接指出錯誤，而是引導 Author 思考背後的原因。例如，不要說「這裡應該用 A 而不是 B」，而要說「這裡用 B 的話，可能會導致 X 問題，考慮一下用 A 是否更合適」。
*   **提出具體的建議**：不要只說「這段程式碼需要重構」，而要說「這段程式碼的耦合度太高，可以考慮將 X 功能抽象成一個獨立的模組」。
*   **使用肯定語氣**：先肯定程式碼的優點，再提出改進建議。例如，「這段程式碼的單元測試寫得很完整，很好！不過，Y 功能的測試案例可以再補充一些」。
*   **使用程式碼片段輔助說明**：直接在程式碼中標記問題，並附上修改建議。

讓我們來看一個例子。假設有這樣一段 Python 程式碼：

```python
def calculate_discount(price, is_member):
  if is_member:
    discount = price * 0.1
  else:
    discount = 0
  return price - discount
```

**差的 Review Comment:**

> 這段程式碼寫得太冗長了！

**好的 Review Comment:**

> 這段程式碼可以更簡潔一些。可以考慮使用三元運算符：`discount = price * 0.1 if is_member else 0`。這樣可以讓程式碼更易讀。另外，可以考慮將折扣比例提取成一個常數，方便後續維護。例如：`MEMBER_DISCOUNT_RATE = 0.1`。

好的 Review Comment 不僅指出了問題，還提供了具體的解決方案，並且解釋了「為什麼」要這樣做。

## 被 Review 的心態：擁抱成長的機會

被 Review 的時候，難免會感到有些壓力。但請記住，Code Review 不是對你的否定，而是團隊幫助你成長的機會。以下是一些建議：

*   **保持開放的心態**：不要 defensive，虛心接受 Reviewer 的回饋。
*   **積極提問**：如果對 Reviewer 的回饋有疑問，不要害怕提問。
*   **將 Review 回饋視為學習機會**：從 Review 中學習新的知識、新的技術、新的設計模式。
*   **感謝 Reviewer 的付出**：花時間 Review 你的程式碼，是對你的幫助。

## 情境分析：表層 Review vs 深層 Review

讓我們來看一個更複雜的例子，展示表層 Review 和深層 Review 的差異。假設我們正在開發一個電商網站的商品搜尋功能。以下是一段 TypeScript 程式碼：

```typescript
class ProductSearch {
  constructor(private products: Product[]) {}

  search(query: string): Product[] {
    const results: Product[] = [];
    for (const product of this.products) {
      if (product.name.toLowerCase().includes(query.toLowerCase())) {
        results.push(product);
      }
    }
    return results;
  }
}
```

**表層 Review:**

> 1.  `toLowerCase()` 方法重複調用了兩次，可以提取成一個變數。
> 2.  可以考慮使用 `Array.filter()` 方法，讓程式碼更簡潔。

**深層 Review:**

> 1.  `toLowerCase()` 方法重複調用了兩次，可以提取成一個變數。（同意表層 Review 的第一點）
> 2.  可以考慮使用 `Array.filter()` 方法，讓程式碼更簡潔。（同意表層 Review 的第二點）
> 3.  **更重要的是：** 這個 `ProductSearch` 類別的設計存在一些問題。它直接依賴於 `Product` 陣列，耦合度太高。如果我們需要從資料庫、API 等不同的來源獲取商品資料，就需要修改這個類別。可以考慮使用依賴注入 (Dependency Injection) 的方式，將 `products` 作為一個介面 (Interface) 注入，這樣可以提高程式碼的擴充性和可測試性。例如：

```typescript
interface ProductProvider {
  getProducts(): Product[];
}

class ProductSearch {
  constructor(private productProvider: ProductProvider) {}

  search(query: string): Product[] {
    const products = this.productProvider.getProducts();
    const results: Product[] = [];
    for (const product of products) {
      if (product.name.toLowerCase().includes(query.toLowerCase())) {
        results.push(product);
      }
    }
    return results;
  }
}
```

深層 Review 不僅關注程式碼的語法和風格，更關注程式碼的設計和架構。它能夠幫助團隊成員理解系統的整體架構，並確保程式碼符合團隊的設計規範。

## 結語

Code Review 是一門藝術，需要不斷的學習和實踐。希望今天的分享能幫助大家更有效地運用 Code Review 這個強大的工具，提升團隊的工程能力，塑造良好的工程文化。記住，Code Review 不只是品質門檻，更是團隊成員互相學習、對齊架構認知的最佳場域。讓我們一起努力，讓 Code Review 成為我們團隊的競爭力！

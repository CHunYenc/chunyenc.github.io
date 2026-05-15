---
title: "架構不是畫圖：從 Clean Architecture 到務實的分層設計"
description: "由 AI 生成的深度技術專題 — 架構的目的是服務業務需求，而非滿足工程師對完美的追求。"
date: 2026-05-15T17:56:47+08:00
slug: "ai-clean-architecture-20260515"
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

# 架構不是畫圖：從 Clean Architecture 到務實的分層設計

許多工程師讀完 Clean Architecture 後，往往會陷入一個迷思：為了 Clean 而 Clean，為了抽象而抽象。結果，專案變得過度設計，開發效率反而下降。架構的本質是服務業務需求，而不是滿足工程師對完美的追求。本文將探討如何從 Clean Architecture 的原則出發，落地到務實的分層設計，並強調架構決策紀錄的重要性。

## 依賴反轉原則（DIP）：解耦，而非抽象

依賴反轉原則（Dependency Inversion Principle, DIP）的核心是：高層模組不應該依賴於低層模組，二者都應該依賴於抽象。抽象不應該依賴於細節，細節應該依賴於抽象。

許多人將 DIP 理解為「為了抽象而抽象」。例如，為了遵循 DIP，將所有資料庫操作都抽象成一個 Repository 介面。這本身沒有錯，但如果這個 Repository 介面只是簡單地包裝了底層的資料庫操作，而沒有提供任何額外的價值，那麼這種抽象就是不必要的。

DIP 的真正意義在於**解耦**。解耦的目的是為了讓高層模組更容易測試、更容易修改、更容易擴充。如果抽象層沒有帶來這些好處，那麼就沒有必要引入。

## 分層設計的取捨：3 層架構 vs. Hexagonal Architecture

分層架構是一種常見的軟體架構模式，它將應用程式劃分為多個層次，每個層次都有特定的職責。常見的分層架構包括 3 層架構和 Hexagonal Architecture（又稱 Ports and Adapters Architecture）。

**3 層架構**通常包括：

*   **表示層（Presentation Layer）：** 負責處理使用者介面和使用者輸入。
*   **業務邏輯層（Business Logic Layer）：** 負責處理應用程式的核心業務邏輯。
*   **資料存取層（Data Access Layer）：** 負責處理資料庫操作。

3 層架構簡單易懂，適用於小型專案。但當專案規模變大時，3 層架構可能會變得難以維護，因為業務邏輯層和資料存取層之間的耦合度很高。

**Hexagonal Architecture** 則將應用程式的核心業務邏輯與外部依賴（例如資料庫、使用者介面）隔離開來。它通過 Ports 和 Adapters 來實現這種隔離。

*   **Ports：** 定義了應用程式核心與外部世界之間的介面。
*   **Adapters：** 實現了這些介面，並將應用程式核心與特定的外部技術連接起來。

Hexagonal Architecture 更加靈活，適用於大型專案。但它也更複雜，需要更多的設計和實作工作。

**什麼時候 3 層架構就夠了？什麼時候需要 Hexagonal Architecture？**

這取決於專案的複雜度和未來可能的變更。如果專案很小，而且不太可能需要變更資料庫或使用者介面，那麼 3 層架構就足夠了。但如果專案很大，而且未來可能需要變更資料庫或使用者介面，那麼 Hexagonal Architecture 可能是更好的選擇。

**過度分層導致開發效率下降 vs 適度分層帶來長期收益：一個情境**

假設我們正在開發一個電商網站的訂單管理系統。

**情境一：過度分層**

為了追求絕對的 Clean Architecture，我們將所有資料庫操作都抽象成 Repository 介面，並為每個資料庫表都建立一個 Repository 類別。結果，我們需要編寫大量的樣板程式碼，而且這些程式碼並沒有帶來任何額外的價值。開發一個簡單的訂單查詢功能，需要修改多個檔案，增加了開發時間和維護成本。

**情境二：適度分層**

我們只在需要解耦的地方進行抽象。例如，我們將訂單的狀態管理邏輯抽象成一個 Service 介面，並提供不同的實作來處理不同的訂單狀態。這樣，我們可以很容易地新增新的訂單狀態，而不需要修改底層的資料庫操作。開發一個簡單的訂單查詢功能，只需要修改少數幾個檔案，大大提高了開發效率。

**程式碼對比：業務邏輯與基礎設施高度耦合 vs 清晰分離關注點**

**版本一：業務邏輯與基礎設施高度耦合 (Python)**

```python
import sqlite3

def get_order(order_id):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    order = cursor.fetchone()
    conn.close()
    return order

def update_order_status(order_id, status):
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET status=? WHERE id=?", (status, order_id))
    conn.commit()
    conn.close()

# 業務邏輯直接調用資料庫操作
order = get_order(123)
if order and order[2] == 'pending': # order[2] 是 status
    update_order_status(123, 'processing')
```

**版本二：清晰分離關注點 (Python)**

```python
from abc import ABC, abstractmethod

class OrderRepository(ABC):
    @abstractmethod
    def get_order(self, order_id):
        pass

    @abstractmethod
    def update_order_status(self, order_id, status):
        pass

class SQLiteOrderRepository(OrderRepository):
    def __init__(self, db_path):
        self.db_path = db_path

    def get_order(self, order_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
        order = cursor.fetchone()
        conn.close()
        return order

    def update_order_status(self, order_id, status):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET status=? WHERE id=?", (status, order_id))
        conn.commit()
        conn.close()

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def process_pending_order(self, order_id):
        order = self.order_repository.get_order(order_id)
        if order and order[2] == 'pending':
            self.order_repository.update_order_status(order_id, 'processing')

# 業務邏輯通過 OrderService 和 OrderRepository 交互
order_repository = SQLiteOrderRepository('orders.db')
order_service = OrderService(order_repository)
order_service.process_pending_order(123)
```

版本二雖然程式碼量更多，但關注點分離更清晰。業務邏輯不再直接依賴於具體的資料庫實作，更容易測試和修改。如果未來需要更換資料庫，只需要修改 `SQLiteOrderRepository` 即可，而不需要修改業務邏輯。

## 架構決策紀錄（ADR）：為什麼比怎麼更重要

架構決策紀錄（Architecture Decision Record, ADR）是一種記錄架構決策的文件。它記錄了為什麼做出這個決策，以及這個決策的替代方案和後果。

ADR 的重要性在於：

*   **知識傳承：** 讓團隊成員了解架構決策的背景和原因。
*   **可追溯性：** 方便追蹤架構決策的演變過程。
*   **避免重複決策：** 避免團隊成員重複做出相同的決策。

ADR 的格式可以很簡單，只需要包含以下幾個部分：

*   **標題：** 簡要描述決策。
*   **背景：** 描述決策的背景和問題。
*   **決策：** 描述做出的決策。
*   **替代方案：** 描述考慮過的替代方案。
*   **後果：** 描述決策的後果。

例如，一個 ADR 可能會記錄為什麼選擇使用 PostgreSQL 作為資料庫，而不是 MySQL。它會描述 PostgreSQL 的優點和缺點，以及 MySQL 的優點和缺點，並解釋為什麼最終選擇了 PostgreSQL。

**為什麼「為什麼這樣設計」比「怎麼設計」更重要？**

因為「怎麼設計」是可以改變的，但「為什麼這樣設計」的理由卻是恆定的。理解了「為什麼」，才能更好地適應變化，做出正確的決策。

## 結論

架構不是畫圖，而是解決問題。好的架構不是看起來厲害，而是讓團隊能快速且安全地迭代。要做到這一點，需要理解 Clean Architecture 的原則，並將其落地到務實的分層設計中。同時，要重視架構決策紀錄，記錄「為什麼這樣設計」，而不是只關注「怎麼設計」。只有這樣，才能建立一個可維護、可擴充的軟體系統。

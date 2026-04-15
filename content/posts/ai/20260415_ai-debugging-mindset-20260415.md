---
title: "除錯的藝術：從盲目 print 到系統性問題分析"
description: "由 AI 生成的深度技術專題 — 除錯能力不是天賦，而是一套可以被訓練的系統性思維。"
date: 2026-04-15T17:37:21+08:00
slug: "ai-debugging-mindset-20260415"
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

# 除錯的藝術：從盲目 print 到系統性問題分析

各位工程師朋友們，大家好。在大型分散式系統中，生產環境的 Bug 就像家常便飯。經歷過幾次半夜被 call醒，看著儀表板一片紅，心跳加速的經驗後，我深刻體會到，除錯能力不是天賦，而是一套可以被訓練的系統性思維。今天，我想分享一些我在實戰中總結的經驗，希望能幫助大家擺脫「盲目 print」，建立一套更有效率的除錯流程。

## 問題定位的思維框架

當 Bug 發生時，最忌諱的就是慌亂。首先，我們要建立一套清晰的思維框架，幫助我們快速縮小問題範圍。

*   **二分法：** 這是最基礎也是最有效的策略。如果問題發生在 A 和 B 之間，先確認 A 是否正常，再確認 B 是否正常。如果 A 正常但 B 不正常，問題就一定在 B 內部或 B 的依賴項。不斷重複這個過程，就能快速定位到問題的根源。
*   **假設驅動：** 不要盲目地猜測，而是基於現有的資訊，提出合理的假設。例如，「API 超時可能是因為資料庫連線池耗盡」，然後設計實驗去驗證這個假設。如果假設被證偽，就重新審視現有的資訊，提出新的假設。
*   **最小可重現案例 (Minimal Reproducible Example)：** 盡可能將問題簡化到最小的範圍，建立一個可以穩定重現問題的案例。這不僅可以幫助你更好地理解問題，也能方便你與其他工程師溝通。

## Observability 三本柱：Logging、Metrics、Tracing

在分散式系統中，單靠肉眼和 print 是不可能完成除錯任務的。我們需要借助 Observability 三本柱：Logging、Metrics 和 Tracing。

*   **Logging：** 記錄應用程式的運行狀態。好的 Logging 應該包含足夠的上下文資訊，例如請求 ID、使用者 ID、時間戳記、錯誤碼等等。但是，過多的 Logging 也會影響效能，所以需要權衡。
*   **Metrics：** 監控應用程式的效能指標，例如 CPU 使用率、記憶體使用率、請求延遲、錯誤率等等。Metrics 可以幫助我們快速發現異常，並判斷問題的嚴重程度。
*   **Tracing：** 追蹤請求在不同服務之間的調用鏈路。Tracing 可以幫助我們定位到瓶頸，並找出導致錯誤的服務。

這三者並非獨立存在，而是相互補充。Metrics 可以幫助我們發現異常，Logging 可以提供詳細的上下文資訊，Tracing 可以追蹤請求的調用鏈路。只有將它們結合起來使用，才能真正實現全方位的監控和除錯。

## 生產環境除錯的紀律

生產環境除錯是一項高壓力的工作。在壓力下，我們很容易犯錯，導致問題變得更加複雜。因此，我們需要建立一套嚴格的紀律，避免「修東牆補西牆」。

*   **保持冷靜：** 深呼吸，不要慌張。先花幾分鐘時間，仔細閱讀錯誤訊息和日誌，嘗試理解問題的本質。
*   **小步快跑：** 不要一次性修改大量的程式碼。每次只修改一小部分，然後進行測試，確認修改是否有效。
*   **記錄所有操作：** 記錄你所做的所有操作，包括修改的程式碼、執行的命令、觀察到的現象等等。這可以幫助你回溯問題，並避免重複犯錯。
*   **事後檢討：** 問題解決後，花時間進行事後檢討。分析問題的根本原因，並制定預防措施，避免類似的問題再次發生。

## 實戰情境：API 間歇性超時

假設我們有一個 API，間歇性地出現超時錯誤。使用者回報說，有時候請求會卡住，需要重新整理才能正常工作。

1.  **Metrics 告警：** 我們首先從 Metrics 儀表板上看到，API 的平均延遲明顯上升，並且出現了大量的 504 Gateway Timeout 錯誤。
2.  **Tracing 分析：** 我們使用 Tracing 工具，追蹤一個超時的請求。發現請求在調用下游服務 A 時，耗時異常。
3.  **Logging 調查：** 我們查看服務 A 的日誌，發現大量的資料庫連線池耗盡的錯誤。
4.  **假設驗證：** 我們懷疑是資料庫連線池配置不足導致了超時。我們增加了資料庫連線池的大小，並重新部署了服務 A。
5.  **監控驗證：** 部署後，我們持續監控 API 的延遲和錯誤率。發現延遲明顯下降，錯誤率也恢復正常。

在這個案例中，我們結合了 Metrics、Tracing 和 Logging，成功定位並解決了 API 超時的問題。

## 程式碼範例：錯誤處理的差異

以下是一個簡化的 Python 範例，展示了 Junior 工程師和 Senior 工程師在處理錯誤時的差異。

**Junior 版（缺乏錯誤處理）：**

```python
import requests

def get_user_data(user_id):
  response = requests.get(f"https://api.example.com/users/{user_id}")
  data = response.json()
  return data
```

這個版本沒有任何錯誤處理，如果 API 請求失敗，程式就會直接崩潰。

**Senior 版（有完整 logging 與 graceful degradation）：**

```python
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_data(user_id):
  try:
    response = requests.get(f"https://api.example.com/users/{user_id}", timeout=5)
    response.raise_for_status()  # 檢查 HTTP 狀態碼
    data = response.json()
    logging.info(f"成功獲取使用者 {user_id} 的資料")
    return data
  except requests.exceptions.RequestException as e:
    logging.error(f"獲取使用者 {user_id} 的資料失敗: {e}")
    # 降級處理：返回預設值或從快取讀取
    return {"error": "無法獲取使用者資料"}
  except ValueError as e:
    logging.error(f"解析使用者 {user_id} 的資料失敗: {e}")
    return {"error": "資料格式錯誤"}
```

這個版本增加了錯誤處理、Logging 和 graceful degradation。如果 API 請求失敗，程式會記錄錯誤訊息，並返回預設值，避免程式崩潰。`response.raise_for_status()` 檢查 HTTP 狀態碼，確保請求成功。`timeout=5` 設定請求超時時間，避免請求一直卡住。

這個例子展示了，好的錯誤處理不僅可以提高程式的穩定性，還可以幫助我們更好地除錯。

## 總結

除錯是一項需要不斷學習和實踐的技能。希望今天的分享能幫助大家建立一套更有效率的除錯流程，從「盲目 print」走向系統性的問題分析。記住，除錯能力不是天賦，而是一套可以被訓練的系統性思維。 多練習，多思考，你也能成為一位優秀的除錯專家。

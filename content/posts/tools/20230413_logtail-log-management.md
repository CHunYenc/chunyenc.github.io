---
title: "Logtail - 一個彙整免費 Paas 平台的日誌平台"
description: "筆者從 papertrailapp 毫不猶豫直接跳到 logtail."
date: 2023-04-13T02:46:15Z
slug: logtail-log-management
categories:
    - Experience
tags:
    - Logtail
    - Render.com
    - Heroku
hidden: false
comments: true
draft: true
---

# 前言

因筆者有使用 Heroku、Render.com、Railway 的經驗，那他們都是 PaaS (Platform as a Service，平台及服務) 的服務平台。

> 這些 PaaS 平台通常提供了開發工具、執行環境、資料庫、身份驗證、監控等服務，讓開發人員可以專注於應用程式的開發，而不必擔心基礎架構的建設。

筆者在這邊有分配不同平台的使用情境：(沒列就是我沒使用 ..)

- `Heroku`：主要負責應用上線 `學生身分免費`
- `Render.com`：主要負責應用上線、靜態網站 `免費`
- `Railway.app`：主要負責 RDBMS 資料庫 (PostgreSQL)、快取資料庫 (Redis) `免費`
  - **Railway.app** 目前有推薦機制，筆者的推薦連結 --> https://railway.app?referralCode=37Lpxy
  - **Railway.app 目前還沒有支援 log stream**

那可以知道我在 PaaS 的部份用的非常兇猛，甚至 logging 非常分散，但是 `機器不同源，日誌是類似`。所以我需要一個有效的方式來`收集`、`管理`和`分析`這些日誌，以便進行`錯誤排查`、`性能優化`和`安全監控`等。

接下來就是要來講比較實際的 Logtail 的 `使用過程(串接)` 到 `好處(優點)`。

# 好處一：無痛串接 Paas 平台

## Heroku

綁定 `Heroku` 前，先到 `Logtail` 申請後就可以直接來用了 .. (如下圖)

![綁定的過程](/images/20230413_logtail/01.png)

所以你只要做四件事：

1. 把你的應用程式部屬到 `Heroku`，確定可以使用 !
2. 到 `Logtail` 申請一個 `來源(Sources)`，依照上圖的步驟操作一次。
3. 然後你就不斷地在 `1 步驟` 的應用程式不斷刷新頁面.
4. 觀察 Logtail 有沒有新增加 logging.


## Render.com

```
待補，但基本上跟上面一樣 ..
```

# 好處二：內建 Grafana 視覺化平台

Grafana 是一個流行的開源數據視覺化和監控平台，它提供了`強大的儀表板`和`視覺化工具`。

我今天也主要不是探討這個平台，自己用的也不是非常熟。

> 筆者使用 papertrailapp 只能串接到自己的視覺化平台，超貴。

# 好處三：異常通知

> papertrailapp 一樣有。

# 好處三：其他平台有的基本上都有 ..


# 缺點：錢


# 建議：自架

主要還是回到錢的部分，一個月 24 USD 真的不便宜。

目前是有朝向 Graylog(`ElasticSearch` or `OpenSearch`) + Grafana 來建。

這邊之後再給大家講一下我的架構。
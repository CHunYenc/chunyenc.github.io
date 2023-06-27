---
title: "Line Notify - 如何簡單使用 Line Notify 自動化通知"
description: "Line Notify 自動化通知超級好用 ~"
date: 2023-01-16T00:02:09+08:00
slug: "line-notify"
categories:
    - LINE
tags:
    - LINE
math: 
license: 
hidden: false
comments: true
draft: true
---

# Line Notify

[LINE Notify 官方網址](https://notify-bot.line.me/zh_TW/)

[LINE Notify API 說明文件](https://notify-bot.line.me/zh_TW/)

# 前言

Line Notify 是由程式發送通知訊息至我們的 Line 帳號內，是 Line 免費的服務，我們可以將重要訊息或是定時監控傳送至我們手機上，隨時掌握最新狀態。

## 重點整理

以下整理 LINE Notify 的注意事項。

- 推出服務公司：`LINE`
- 收費：`免費` (至少在目前 2023/06/27 免費)
- 功能：`發送訊息`，不可互動。 (互動屬於 Line Bot)
- 通知對象：`個人`、`群組`

# 使用教學

以下先列出使用 Line Notify 的步驟，後面在附上詳解。

1. 登入 Line Notify 官方網頁
2. 取得權杖 (Token)
3. 複製權杖
4. 收到 Line Notify 綁定成功的訊息
5. 在 APP 儲存這個權杖，需要通知時拿它來發送

# 詳細步驟

## 登入 Line Notify 官方網頁

> 補圖

點擊後右上角進行登入。

> 補圖

登入頁面如下。

> 補圖

## 取得權杖 (Token)

登入完成後，你可以直接點擊右上角的個人頁面。

> 補圖

點擊發行權杖。

> 補圖

選擇通知 `使用者` 或 `群組`。

> 記得綁定群組時，要把 Line Notify 在 LINE 中的帳號加入群組裡面。

> 補圖

## 複製權杖

當上面的選擇都處理好後，你會產生一個權杖。

這時候把這個權杖複製下來 ~ !

> 補圖

## 收到 Line Notify 綁定成功的訊息

在輸出權杖的同時，你也會收到 Line Notify 的訊息。

> 補圖

## 在 APP 儲存這個權杖，需要通知時拿它來發送

我這邊重新申請一個 Token，為了來完成本文章。

名稱：`測試通知用`
對象：`我自己`

> 補圖

我的權杖如下，接下來使用這個權杖給我一個測試訊息。

> 補圖

打開 POSTMAN。

輸入 `POST` 網址為： `https://notify-api.line.me/api/notify`

點擊 `Authorization`，選擇左方 `Type` 為 `Bearer Token`，再把剛剛的權杖貼在右邊。(如下圖)

> 補圖

還沒完成，我們還沒輸入我們想要傳送的訊息。

點擊 `Body`，選擇 `form-data`，新增一個 `Key` 為 `message`。內容為 `今天是20230627，天氣非常好。`

最後點擊 `Send`。

> 補圖

然後 LINE 上就出現我們剛剛想輸入的訊息囉 !

> 補圖

# 參考網址

[[C#][Line] 如何發送 Line Notify 通知訊息 (開發人員用)](https://blog.hungwin.com.tw/csharp-line-notify/)

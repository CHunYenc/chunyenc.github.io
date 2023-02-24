---
title: "Cloudflare - 架設 Google-blogger 與 Github-page DNS 困難排除"
description: ""
date: 2023-01-16T00:02:09+08:00
slug: "cloudflare-dns-error"
categories:
    - Experience
tags:
    - Cloudflare
math: 
license: 
hidden: false
comments: true
draft: false
---

# 前言

主要是有應用架設在 `Heroku`, 發現他要所謂 `Server Name Indication (SNI)` 的方式來部署 `HTTPS`。

> 結論就是 `DNS` 從 `Google Domains` 換成 `Cloudflare`，然後碰到`轉址`、`HTTPS`的問題。

透過 `Cloudflare` 弄上 `HTTPS` 時，發現 `Blogger`、`Github page` 都不能正常瀏覽。

因為 `Blogger`、`Github Page` 本身就可以加上 `HTTPS`，但是加上 `HTTPS` 後一直不能瀏覽。

然後 `HTTPS` 是可以正常瀏覽。

## 問題特徵

將前言的整理一下，`如果你有下面的問題，可以參考我怎麼解決的！`

1. `http` 可以正常瀏覽頁面。
2. 改成 `https` 無法瀏覽頁面。顯示`「這個網頁無法正常運作」`。
    - 使用 `blogger` 
      - 步驟 1 - 進入 `設定`
      - 步驟 2 - `HTTPS 重新導向` 開啟
    - 使用 `Github`
      - 步驟 1 - 點擊儲存庫 `YOURGITHUBNAME.github.io`
      - 步驟 2 - 進入 `Settings`
      - 步驟 3 - 點擊 `Pages`, 設定頁面並加入自定義 `domain`. 
      - 步驟 4 - `Enforce HTTPS` 開啟

關於第 `2` 點。不管是 blogger、Github 都會導致`「這個網頁無法正常運作」`的狀況。

> 如果你的狀況跟我很類似，或許你可以試試看 !

# 設定方式

## 將 `SSL/TLS` 改為 `FULL` 模式

![Cloudflare SSL/TLS 設定](images/20230116/01-full.jpg)

我原本的設定是 `Flexible (彈性)` 模式。

關於 Flexible 模式的說明，其實 `Cloudflare` 官方文檔有提到碰到的問題。

[Flexible 模式](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/flexible/)

`Flexible` 雖然開啟後好用，可以將 `HTTP` 的網頁透過 `Cloudflare` 的處理後變成 `HTTPS`。

但是原本的網頁已經有 `HTTPS` 時，就要透過 `FULL` 模式去做處理。

> 如果你的網頁都是使用 `HTTP`，那麼你可以預設 `Flexible`。

## 路由規則

了解路由規則時，先釐清自己的使用需求是不是符合。

我的主網域：[https://chunyen.xyz](https://chunyen.xyz) (Github Page，有 `HTTPS`)

我的子網域：[https://b.chunyen.xyz ](https://b.chunyen.xyz ) (Blogger，有 `HTTPS`)

我的子網域：[http://p.chunyen.xyz](https://p.chunyen.xyz) (自己的應用，無 `HTTPS`)

假設我的網頁、部落格內建的 `HTTPS` 較多，其實我就直接使用 `FULL` 模式。

若是相反呢？我就使用 `Flexible`。

> 再透過 Cloudflare 路由規則將指定的網頁設定成其他模式 ! 只有三個的扣打可以使用其他模式。

步驟：
1. 點擊 `規則`
2. 再點擊 `網頁規則` 同一頁的 `建立網頁規則`
3. `填入 URL` 後，記得要選取 `挑選設定` 的 `SSL` 為你要設定的模式。

![Cloudflare SSL/TLS 路由規則](images/20230116/03-rule-example.jpg)

接下來應該沒問題了 ! 免費時間等超久。

> 但是免費的還是等吧 xD

## 最後的設定

![Cloudflare SSL/TLS 路由規則的結果](images/20230116/04-result.jpg)

1. 我將 `SSL/TLS` 設定為彈性。
2. 另外透過兩個 `路由規則` 來設定我的 `blogger`、`github page` 的網頁

> 路由規則的部分剩下一個扣打。

若依照我的設定，應該你的網頁就可以正常瀏覽了！

花了非常多時間。但沒想到 `Cloudflare` 提供這麼多免費的服務，之前一直有看到這間公司的 Logo，但一直沒機會使用。

# 完成 !
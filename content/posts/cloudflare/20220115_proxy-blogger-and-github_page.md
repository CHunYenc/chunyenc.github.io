---
title: "Cloudflare - 架設 Google-blogger 與 Github-page DNS 困難排除"
description: ""
date: 2023-01-16T00:02:09+08:00
slug: "git-deleted-commit-big-files"
categories:
    - Experience
tags:
    - GIT
math: 
license: 
hidden: false
comments: true
draft: true
---

# 前言

主要是有應用架設在 Heroku, 發現他要所謂 Server Name Indication (SNI) 的方式來部署 `https`。

> 結論就是 DNS 從 Google Domains 換成 Cloudflare, 然後碰到一些問題。

透過 `cloudflare` 弄上 `https` 時，發現 `blogger`、`Github page` 都不能正常瀏覽。

因為 `blogger`、`Github page` 本身就可以加上 `https`，但是加上 `https` 後一直不能瀏覽。

然後 `http` 是可以正常瀏覽。

## 問題特徵

將前言整理成問題的特徵。

1. http 可以正常瀏覽頁面。
2. 改成 https 無法瀏覽頁面。顯示`「這個網頁無法正常運作」`。
    - 使用 `blogger` 
      - 步驟 1 - 進入 `設定`
      - 步驟 2 - `HTTPS 重新導向` 開啟
    - 使用 `Github`
      - 步驟 1 - 點擊儲存庫 `YOURGITHUBNAME.github.io`
      - 步驟 2 - 進入 `Settings`
      - 步驟 3 - 點擊 `Pages`, 設定頁面並加入自定義 `domain`. 
      - 步驟 4 - `Enforce HTTPS` 開啟

`2.` 不管是 blogger、Github 都會導致`「這個網頁無法正常運作」`的狀況。

> 如果你的狀況跟我很類似，或許你可以試試看 !

# 設定方式

## 將 `SSL/TLS` 改為 `FULL` 模式

![](images/post/cloudflare/01-full.jpg)
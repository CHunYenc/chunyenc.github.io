---
title: "Jenkins 架設紀錄 02 - 讓作業偵測 Github 有無新的動作，有的話就自動執行作業"
description: "主要透過 Github Webhook 讓 Jenkins 觸發抓取我的 Github"
date: 2022-06-26T14:45:17+08:00
slug: "jenkins-02"
image: "jenkins.png"
categories:
    - CICD
tags:
    - Jenkins
hidden: false
comments: true
draft: true
---

# 內容

畢竟身為一個工程師，不管是在 Github 還是內部的 Gitea、Gitlab 再配上 Jenkins 自動幫你部署，
讓你絲毫不費力地讓主管看到你今天做的成品的時候 ...

真是舒服 XD
今天只是打一下我建立作業，並配上 Webhook 的一些設定流程。

# 流程

今天 Clone 的庫，是我的加密貨幣抓取網頁。

主要目的就只是要讓 Google Sheet 透過 XML 的方式同步加密貨幣的價格建立的網站。

連結：[CHunYenc/crypto-price-scheduler](https://github.com/CHunYenc/crypto-price-scheduler)

## 建立一個新的作業「Clone-Crypto-Price-Schedule」

```
參考「參考文獻 1」來設定 Github Webhook 與 Jenkins 的連線
```
到 Github 你要 Clone 的 repository

## 申請 ngrok

Webhooks 不支持無 https 的網址, 所以一樣要使用 ngrok 替代

## 安裝 ngrok on Ubuntu

這邊紀錄一下我在 Ubuntu 安裝 ngrok 的過程，畢竟這套 ngrok 真的很好用 !!!

ngrok download 官方連結：[https://ngrok.com/download](https://ngrok.com/download)

建議還是找官方安裝，可以點擊我上面的官方連結過去 copy.

我是使用
```

```

## 回到 Github 設定 Webhooks



```
回到 Github settings add Webhooks 
https://xxxx.jp.ngrok.io/github-webhook/
(記得加上 /github-webhook/)
```

# 參考文獻

1. [透過 GitHub Webhook 讓你 push code 到 Github 就會自動觸發本地 Jenkins Pipeline](https://zoejoyuliao.medium.com/%E9%80%8F%E9%81%8E-github-webhook-%E8%A7%B8%E7%99%BC%E6%9C%AC%E5%9C%B0-jenkins-pipeline-%E8%AE%93%E4%BD%A0-push-code-%E5%88%B0-github-%E5%B0%B1%E6%9C%83%E8%87%AA%E5%8B%95%E8%B7%91-ci-cd-7c4bd7a22446)
2. 
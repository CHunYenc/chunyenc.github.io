---
title: "JenKins 架設紀錄 04 - 建立 Jenkins Agent"
description: "主要是工作想要上線 Jenkins 讓我的專案能夠更快速上線"
date: 2022-06-21T21:28:00+08:00
slug: "jenkins-04-agent"
categories:
    - CICD
tags:
    - Jenkins
math: 
license: 
hidden: false
comments: true
draft: true
---

# 前言

前一篇「JenKins 架設紀錄 01 - 使用 Docker 架設 Jenkins 並第一次使用」發出也已經過了非常久了，今天要來嘗試使用 Jenkins Agent，來部署我的小應用程式。

連結：[CHunYenc/crypto-price-scheduler](https://github.com/CHunYenc/crypto-price-scheduler)

說明：主要是幫我爬取 Binance、Crypto.com 交易所的加密貨幣交易對價錢。然後再透過 Google Sheet 使用 ```IMPORTXML``` 的公式導入現在價格。

之後會再寫一篇如何來使用 ```crypto-price-scheduler``` 這個小系統。

# 開始

## 進入管理 Jenkins

首先就是先進入 Jenkins 左邊的「管理 Jenkins」。

![管理 Jenkins](/images/20220621/01-Configuration.png)

```
點擊「管理節點」
```

![管理節點](/images/20220621/02-nodes.png)

## 新增節點

```
這邊當然會發現我們只有一台，因為根本還沒加入其他節點。

這邊直接點擊「新增節點」，並且新增一台空的節點。
```

```空的節點：就是直接新增。```

![新增節點](/images/20220621/03-new-agent.png)

```
什麼都不要填，直接 save。
```

![建立好無法連線的 Agent](/images/20220621/04-created-agent.png)

```
點擊剛剛建立的 Agent，會跳出我們要連線的 Agent 的 secret-file
```

![查看 Agent 的連線資訊](/images/20220621/05-agent-information.png)

```
有點多資訊要擋，不好意思。

不過基本上我們要複製 echo 右邊的那一串 secret-file。
```

複製完之後，讓我們在 Agent 機器上使用 Docker 建立 Jenkins Agent。

先上範例，複製的在下面

```
# my example

docker run --init jenkins/inbound-agent -url http://xxx.chunyen.xyz:8080/ -workDir=/home/jenkins/agent 39a5a3xxxxxxxxx6c308187 xxx.chunyen.xyz
```

```--init```

```-url```

```--workDir```

```
# copy

docker run --init jenkins/inbound-agent -url <url> -workDir=/home/jenkins/agent <secret-file> <agent-name>
```

docker run 執行完後，就會發現我們已經連線成功了！

![Agent 連線成功](/images/20220621/06-agent-ok.png)

```
下一篇，就要來建立 pipeline 了 !!!
```

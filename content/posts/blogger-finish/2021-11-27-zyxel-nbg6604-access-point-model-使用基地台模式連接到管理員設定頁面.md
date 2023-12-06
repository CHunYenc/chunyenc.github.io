---
title: "ZYXEL NBG6604 Access Point Model 使用基地台模式連接到管理員/設定頁面"
date: 2021-11-27T14:22:00Z
updated: 2021-11-27T14:22:46Z
blogimport: true 
categories:
  - Experience
tags: 
  - Network
  - ZYXEL
  - NBG6604
  - Access-Point-Model
  - AP-Model
slug: "zyxel-nbg6604-access-point-model-connect-to-admin-page"
draft: false
---

## 說明

不廢話，先說明一下為什麼會碰到這個問題，實際原因不太了解。真的對網路只是微懂。

而本篇主要是記錄這問題是如何解決的，並從哪裡得到這些資訊及解決方式。

機型：ZYXEL NBG6604

## 原因

主要是因為在設定家裡網路時，發現抓不到網路印表機，

因為印表機在不同網域底下（直插光纖小烏龜）目前則是無法達到讓 WIFI 能夠列印，

所以將分享器從「路由器模式」切換成「基地台模式」。

但是這邊發生一點小插曲，就是更改成「基地台模式（Access Point Model）」，

我無法使用 <http://myrouter> 進入管理員頁面。

這個時候只要用網路線/WIFI的方式連線上分享器，使用電腦更改連線IP，以下為我的設定

![設定固定 IP](images/blogger/20211127_zyxel-ngb6604/01.setting-static-ip.png)

IP（IP Address）：192.168.1.254

子網路遮罩（Subnet mask）：255.255.255.0

路由器（Default Gateway）：192.168.1.2

Gateway 的 IP 在更改 AP模式（Access Point Model） 時有跳出來，請記錄下來。

大致上這樣連線 <http://192.168.1.2> 既可以進入到設定頁面了！

![進入 WIFI Router 設定頁面](images/blogger/20211127_zyxel-ngb6604/02.connect-to-wifi-router.png)

參考影片：[ACCESS POINT Mode on ZyXEL Wireless router | NETVN - YouTube](https://www.youtube.com/watch?v=4WDxZMQChCQ)

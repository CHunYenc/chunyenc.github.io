---
title: "WSL2 紀錄 01 - 將 WSL2 指定 PORT 從 Windows 轉發出來"
description: 
date: 2022-07-26T15:27:00+08:00
slug: "2022-WSL01-PORT-FORWARDING"
image: 
categories:
    - Experience
tags:
    - Windows
    - Port
hidden: false
comments: true
draft: false
---

# 前言

後端 Django 使用 WSL2 建立，但是要讓同事連時，該怎麼處理?

# 處理方法

## 到 WSL2 查詢 IP

```shell
yen@DESKTOP-xxx:/mnt/c/.../$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.24.134.84  netmask 255.255.240.0  broadcast 172.24.143.255
        inet6 fe80::215:5dff:fea3:d5d7  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:a3:d5:d7  txqueuelen 1000  (Ethernet)
        RX packets 43142  bytes 7192731 (7.1 MB)
        RX errors 0  dropped 2  overruns 0  frame 0
        TX packets 1060  bytes 178104 (178.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

...
```

關鍵是在 ```172.24.134.84```，要去記得 WSL2 的 IP 位置。

這邊要記得 HOST 為 ```172.24.134.84```、PORT 為 ```9000```。(你要分享的 PORT)

## 到 Windows

### 轉發 WSL2 的連線位置

以下是範例，進行複製的話，不要複製這個，去樣本複製：

```shell
PS C:\Users\xxx> netsh interface portproxy add v4tov4
listenport=9000 listenaddress=0.0.0.0
connectport=9000 connectaddress=172.24.134.84
```

說明：

- listenport=9000

    listenport 意思為我要讓別人連線的 PORT 是 9000。

- listenaddress=0.0.0.0

    listenaddress 意思為我要讓別人連線的 IP 是 0.0.0.0，就是指你現在 Windows 的 IP

- connectport

    connectaddress 意思為被轉發的 PORT。```填寫 WSL2 的 PORT```

- connectaddress

    connectaddress 意思為被轉發的 IP。```填寫 WSL2 的 IP```

以下是樣本，提供你複製：

```shell
netsh interface portproxy add v4tov4 listenport=xxxx listenaddress=0.0.0.0 connectport=xxxx connectaddress=172.x.x.x
```

## 使用瀏覽器連線你的 IP

### 查看自己 Windows 的 IP

```
PS C:\Users\xxx> ipconfig

Windows IP 設定


乙太網路卡 乙太網路:

   連線特定 DNS 尾碼 . . . . . . . . : 
   連結-本機 IPv6 位址 . . . . . . . : xxxxxxxxxxxxxxxxxxxxxx
   IPv4 位址 . . . . . . . . . . . . : 192.168.1.108
   子網路遮罩 . . . . . . . . . . . .: 255.255.255.0
   預設閘道 . . . . . . . . . . . . .: 192.168.1.254
....

```

> 這邊可以知道我的 IP 是 ```192.168.1.108```

連線到 <http://192.168.1.108:9000>

## 如何刪除剛剛新增的設定

### 查詢新增的 portproxy

```shell
C:\Users\xxx> netsh interface portproxy show v4tov4

接聽 ipv4:             連線到 ipv4:

位址            連接埠      位址            連接埠
--------------- ----------  --------------- ----------
0.0.0.0         9000        172.24.134.84   9000
```

### 刪除 portproxy

```shell
C:\Users\xxx> netsh interface portproxy delete v4tov4 listenport=9000 listenaddress=0.0.0.0
```

### 確認 portproxy 是否刪除

```shell
C:\Users\xxx> netsh interface portproxy show v4tov4

沒顯示任何訊息就是沒有透過 portproxy 轉發的 port 了 !!
```

完成囉！

> 記得如果有將後端或其他應用分享出去時，記得要重新啟動！

# Reference

<https://stackoverflow.com/questions/61002681/connecting-to-wsl2-server-via-local-network>

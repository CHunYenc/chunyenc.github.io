---
title: "【Docker】Macbook Air M1 CPU 使用 Docker 建立 SQL Server"
date: 2021-08-07T21:10:00Z
updated: 2021-08-07T22:25:46Z
image: "images/SQLServer2008Logo.jpeg"
slug: "macbook-air-m1-install-sql-server"
tags: 
  - SQLServer
  - Docker
categories:
  - Experience
blogimport: true 
draft: false
---

圖片來源：<https://zh.wikipedia.org/wiki/Microsoft_SQL_Server>

## 前言

說明一下為什麼會使用到 SQL Server + Macbook Air。

主要是在今年 (2021) 年初買了 Macbook Air M1。

那過了近半年，在目前工作的專案下，對方有提出一個需求就是需要導入 SQL Server，

就想說試試看 M1 是否可以建立 SQL Server 的環境。

## 本文章分為四段

- 檢查您的電腦是否有安裝 Docker
- Docker run
- 使用 dbeaver 開源資料庫管理工具連線 SQL Server Container
- 結束

## 本文開始

### 檢查是否安裝 Docker

合理來說 Macbook Pro 一樣可以參考下面範例，若不行，希望你能留言告訴大家

首先當然先確認電腦是否有安裝 Docker，這邊顯示一下我目前 Docker 的版本

指令：

```bash
Docker -v
```

![Docker 版本](images/blogger/20210807_m1-sqlserver/01.docker-version.png)

未安裝的話這邊提供一下 Docker 官方網站：

[https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/)

暫時不提供安裝教學，官方也寫得非常清楚。

### Docker run

這邊其實當初也找了非常多，最後在

[https://medium.com/geekculture/docker-express-running-a-local-sql-server-on-your-m1-mac-8bbc22c49dc9](https://medium.com/geekculture/docker-express-running-a-local-sql-server-on-your-m1-mac-8bbc22c49dc9)

這篇有發現如何在 M1 安裝 SQL Server，其中他有 Highlight 這一段：

```bash
docker run -e "ACCEPT_EULA=1" -e "MSSQL_SA_PASSWORD=MyPass@word" -e "MSSQL_PID=Developer" -e "MSSQL_USER=SA" -p 1433:1433 -d --name=sql mcr.microsoft.com/azure-sql-edge
```

你如果對 Docker 不是很熟的話，這邊稍微介紹一下當中的用法：

- `docker run`：建立一個 container，而 run 後面的意思下面會依序介紹：

- `-e`：設定環境變數，這邊設定了四個。(環境變數可以參考微軟官方）：
[https://docs.microsoft.com/zh-tw/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-ver15](https://docs.microsoft.com/zh-tw/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-ver15)
- `ACCEPT_EULA`：使用者授權
- `MSSQL_SA_PASSWORD`：SA 資料庫密碼
- `MSSQL_PID`：設定 SQL Server 版本或產品金鑰，請參考上面官方連結
- `MSSQL_USER`：使用者名稱
- `-p 1433:1433`：這邊指的是 host 1433 port 就是等於這個 Container 1433 port
      (host:container 的意思)  
- `-d`：背景執行
- `--name`：container 的名稱，這邊設定 sql
- `mcr.microsoft.com/azure-sql-edge`：就是我們要建立的 image

以上是指令的介紹，那我再分享一下我的 dock run 的指令好了，來一個範例版。

```bash
docker run -e "ACCEPT_EULA=1" -e "MSSQL_SA_PASSWORD=20210807Chunyen" -e "MSSQL_PID=Developer" -e "MSSQL_USER=SA" -p 1433:1433 --name=sqlserver mcr.microsoft.com/azure-sql-edge
```

這邊我更動了兩個環境配置。

- 移除 `-d`：我先看看我們的設定是否有問題，因為密碼不能太簡單
- 更改 `MSSQL_SA_PASSWORD`：設定成自己想要的密碼

首次安裝他需要安裝 image，這邊我們等他一下。

![安裝 sql-server image](images/blogger/20210807_m1-sqlserver/03.docker-install-image-finish.png)

正在下載 image "mcr.microsoft.com/azure-sql-edge"

安裝完後，因為我們是直接 docker run，不是 docker pull。

Docker pull 的指令為下載 image，詳細可以 Google，這邊不介紹此指令。

![sql-server 安裝完成](images/blogger/20210807_m1-sqlserver/03.docker-install-image-finish.png)

接下來出現這個畫面後，沒有跑出任何 Error，我們就可以打開 `dbeaver` (開源資料庫管理工具)

### 使用 dbeaver 開源資料庫管理工具連線 SQL Server Container

這邊就不展示如何安裝 dbeaver。

首先我們先打開 dbeaver，如下圖進行新增連線

![dbeaver 建立連線](images/blogger/20210807_m1-sqlserver/04.dbeaver-connect-db.png)

dbeaver 建立連線

建立連線後點擊 Next，輸入連線資訊。

![dbeaver 設定連線資訊](images/blogger/20210807_m1-sqlserver/05.dbeaver-setting-connect-information.png)

dbeaver 連線 SQL Server

先輸入以下資訊：

- Host： localhost
- Port：1433
- Database：master

再輸入

- User name：sa
- Password：20210807Chunyen （我上面預設的）
  - 輸入完畢點擊 Test Connection
  - 跳出 Connection Test 視窗。
  - 點擊 OK
  - 再點擊 Finish.

接下來 dbeaver 就會連線到你在上面使用 Docker 建立的 SQL Server 囉！

![使用 dbeaver 查看 sql-server schema](images/blogger/20210807_m1-sqlserver/06.dbeaver-sql-server-schema.png)

## 結束

本篇結束，已經連到 SQL Server !!!

可以連線後，就可以繼續做工作的事情囉！

祝福讀完文章的你，一路順風 XD

如果你有碰到任何問題，歡迎你在下面留言！

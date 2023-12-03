---
title: "【Docker】Macbook Air M1 CPU 使用 Docker 建立 SQL Server"
date: 2021-08-07T21:10:00Z
updated: 2021-08-07T22:25:46Z
tags: ["#教學文", "#SQLServer", "#Docker", "#Mac", "#小筆記", "#SQL", "#Macbook", "#M1"]
blogimport: true 
draft: true
---

<!-- <div class="separator">
  <p style="margin-left: 1em; margin-right: 1em;">
    <img alt="SQLServer2008Logo.jpg" data-file-height="109" data-file-width="528" decoding="async" height="52" src="https://upload.wikimedia.org/wikipedia/zh/thumb/8/8e/SQLServer2008Logo.jpg/250px-SQLServer2008Logo.jpg" srcset="
        //upload.wikimedia.org/wikipedia/zh/thumb/8/8e/SQLServer2008Logo.jpg/375px-SQLServer2008Logo.jpg 1.5x,
        //upload.wikimedia.org/wikipedia/zh/thumb/8/8e/SQLServer2008Logo.jpg/500px-SQLServer2008Logo.jpg 2x
      " width="250" />
  </p>
</div> -->
<!-- <p> -->
  <!-- 圖片來源：<a href="https://zh.wikipedia.org/wiki/Microsoft_SQL_Server">https://zh.wikipedia.org/wiki/Microsoft_SQL_Server</a> -->
<!-- </p> -->
# 前言

說明一下為什麼會使用到 SQL Server + Macbook Air。主要是在今年 (2021) 年初買了 Macbook Air M1。

那過了近半年，在目前工作的專案下，對方有提出一個需求就是需要導入 SQL Server，

就想說試試看 M1 是否可以建立 SQL Server 的環境。

## 本文章分為四段

- 檢查您的電腦是否有安裝 Docker
- Docker run
- 使用 dbeaver 開源資料庫管理工具連線 SQL Server Container
- 結束

# 那本文開始

## 檢查是否安裝 Docker

合理來說 Macbook Pro 一樣可以參考下面範例，若不行，希望你能留言告訴大家

首先當然先確認電腦是否有安裝 Docker，這邊顯示一下我目前 Docker 的版本
指令：

```docker
Docker -v
```

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://lh3.googleusercontent.com/-tzhgBnfXcOA/YQ5RfJxhCXI/AAAAAAAARSE/ylkiWI9OzroUZbrIUNZaH1rdyTgekIozACLcBGAsYHQ/%25E6%2588%25AA%25E5%259C%2596%2B2021-08-07%2B%25E4%25B8%258B%25E5%258D%25885.22.16.png" style="margin-left: auto; margin-right: auto;"><img alt="Docker 版本圖片" data-original-height="878" data-original-width="1116" height="504" src="https://lh3.googleusercontent.com/-tzhgBnfXcOA/YQ5RfJxhCXI/AAAAAAAARSE/ylkiWI9OzroUZbrIUNZaH1rdyTgekIozACLcBGAsYHQ/w640-h504/%25E6%2588%25AA%25E5%259C%2596%2B2021-08-07%2B%25E4%25B8%258B%25E5%258D%25885.22.16.png" title="Docker 版本圖片" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Docker 版本<br /><br /></td></tr></tbody></table><div class="separator" style="clear: both; text-align: center;">
  
未安裝的話這邊提供一下 Docker 官方網站：

[https://docs.docker.com/docker-for-mac/install/](https://docs.docker.com/docker-for-mac/install/)

暫時不提供安裝教學，官方也寫得非常清楚。

```
Docker run
```

這邊其實當初也找了非常多，最後在
[https://medium.com/geekculture/docker-express-running-a-local-sql-server-on-your-m1-mac-8bbc22c49dc9](https://medium.com/geekculture/docker-express-running-a-local-sql-server-on-your-m1-mac-8bbc22c49dc9)

這篇有發現如何在 M1 安裝 SQL Server，其中他有 Highlight 這一段：

```
docker run -e "ACCEPT_EULA=1" -e "MSSQL_SA_PASSWORD=MyPass@word" -e "MSSQL_PID=Developer" -e "MSSQL_USER=SA" -p 1433:1433 -d --name=sql mcr.microsoft.com/azure-sql-edge
```

你如果對 Docker 不是很熟的話，這邊稍微介紹一下當中的用法：

docker run：建立一個 container，而 run 後面的意思下面會依序介紹：

- -e：設定環境變數，這邊設定了四個。(環境變數可以參考微軟官方）：
[https://docs.microsoft.com/zh-tw/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-ver15](https://docs.microsoft.com/zh-tw/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-ver15)
- ACCEPT_EULA：使用者授權
- MSSQL_SA_PASSWORD：SA 資料庫密碼
- MSSQL_PID：設定 SQL Server 版本或產品金鑰，請參考上面官方連結<br style="background-color: white; box-sizing: inherit; color: #171717; font-family: &quot;Segoe UI&quot;, SegoeUI, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 14px; outline-color: inherit;" />

- MSSQL_USER：使用者名稱
- -p 1433:1433：這邊指的是 host 1433 port 就是等於這個 Container 1433 port
      (host:container 的意思)  
- -d：背景執行
- --name：container 的名稱，這邊設定 sql
- mcr.microsoft.com/azure-sql-edge：就是我們要建立的 image

大致上就以上，那我這邊再分享一下我的 dock run 的指令好了，來一個範例版。

```
docker run -e "ACCEPT_EULA=1" -e "MSSQL_SA_PASSWORD=20210807Chunyen" -e "MSSQL_PID=Developer" -e "MSSQL_USER=SA" -p 1433:1433 --name=sqlserver mcr.microsoft.com/azure-sql-edge
```

這邊我更動了兩個環境配置。

- -d 移除：我先看看我們的設定是否有問題，因為密碼不能太簡單。
- MSSQL_SA_PASSWORD：更改為自己想要的密碼。

首次安裝他需要安裝 image，這邊我們等他一下。

正在下載 image "mcr.microsoft.com/azure-sql-edge"

安裝完後，因為我們是直接 docker run，不是 docker pull。
Docker pull 的指令為下載 image，詳細可以 Google，這邊不介紹此指令。

SQL Server 建立完成

接下來出現這個畫面後，沒有跑出任何 Error，我們就可以打開 dbeaver (開源資料庫管理工具)

## 使用 dbeaver 開源資料庫管理工具連線 SQL Server Container

這邊就不展示如何安裝 dbeaver。

首先我們先打開 dbeaver，如下圖進行新增連線

dbeaver 建立連線

建立連線後點擊 Next，輸入連線資訊。

dbeaver 連線 SQL Server

先輸入以下資訊：

- Host： localhost
- Port：1433
- Database：master

再輸入

- User name：sa
- Password：20210807Chunyen （我上面預設的）
輸入完畢點擊 Test Connection
跳出 Connection Test 視窗。
點擊 OK
再點擊 Finish.
接下來 dbeaver 就會連線到你在上面使用 Docker 建立的 SQL Server 囉！

本篇結束，已經連到 SQL Server !!!

可以連線後，就可以繼續做工作的事情囉！

祝福讀完文章的你，一路順風 XD

如果你有碰到任何問題，歡迎你在下面留言！

---
title: "JenKins 架設紀錄 01 - 使用 Docker 架設 Jenkins 並第一次使用"
description: "主要是指令與如何使用 Docker + Jenkins 並印出 「Hello Jenkins」"
date: 2022-04-10T19:03:00+08:00
slug: "jenkins-01-deploy"
categories:
    - Experience
    - Learn
tags:
    - Jenkins
hidden: false
comments: true
draft: true

---

# 環境

趁這次假日架設了 Jenkins，但是目前為止 M1 處理器皆不支援。

所以用在學生時期使用的 Oracle Cloud 建立一台虛擬機，以下都可以適用在任何雲端平台來操作。

## Ubuntu 版本

```
# lsb_release -a

No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 18.04.6 LTS
Release: 18.04
Codename: bionic
```

## Docker 版本

```
# docker -v
Docker version 20.10.14, build a224086
```

# 操作

[README 官方閱讀手冊](https://github.com/jenkinsci/docker/blob/master/README.md)

以下皆是參考上面的連結，很重要

## 開始

切記這邊不能使用 ```-d``` 指令，否則會影響到第一次啟動密碼

```
docker run --name jenkins -p 8080:8080 -p 50000:50000 --restart always jenkins/jenkins:lts-jdk11
```

執行後，會顯示下面的資訊，密碼就是第一次啟動 Jenkins 在用的。

```
... logging ...

*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

61e8c8cb00c0417bb4c4719ba8559060

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************
```

先複製 ```61e8c8cb00c0417bb4c4719ba8559060```

如果不小心加上 ```-d``` 後，該怎麼辦 ?

可以參考 [備註](#備註)

## 前往網頁

![等待 Jenkins 上工](/images/20220410/00-wait.png)

![進入 JenKins 的第一個畫面](/images/20220410/01-Unlock.png)

就把 ```61e8c8cb00c0417bb4c4719ba8559060``` 貼進去裡面就完成啟用囉 !

## 不安裝任何插件

直接點擊右上角 x, 到時候我們再一項一項安裝.

![點擊右上角 x 進行下一步](/images/20220410/02-plugin.png)

## 進入首頁

![Jenkins 首頁](/images/20220410/03-home.png)

## 更改 admin 密碼

![更改 admin 登入密碼](/images/20220410/04-change_password.png)

## 建立一個 work

![點擊左上角，新增作業](/images/20220410/05-create-work.png)

## Hello Jenkins

![創建一個作業](/images/20220410/06-create-hello-jenkins.png)

這邊可以直接按「OK」。

## 加入一個 echo shell

![選取 執行 Shell](/images/20220410/07-create-shell.jpeg)

畢竟本篇是要執行一個 echo 「Hello World」。

所以我們還是先照做，此篇只是第一篇的 jenkins XD

![打上 echo Hello Jenkins](/images/20220410/08-echo.jpg)

點擊儲存。

## 執行我們建立的作業 Hello Jenkins

![回到 Dashboard](/images/20220410/09-dashboard.jpg)

```
點擊我們 Hello Jenkins 作業做右邊的執行鈕
重整頁面 (F5)
接者會發現「上次執行成功時間」、「上次建置花費時間」已經有數值，不會像圖片上顯示「無」
```

我們現在去看看我們執行的結果

```
點擊「Hello Jenkins」名稱，進入頁面後。
目光移到「左下角」的「建置歷程」
```

![建置歷程](/images/20220410/11-task-history.png)

這邊我點擊 #1 來看看我們，剛剛的 Hello Jenkins 有沒有執行出來 !!

![建置的結果](/images/20220410/10-success-task.png)

這邊只是大致上介紹一下，Jenkins 可以協助你啟動任何的任務，不只是 Shell.

未來我還會再增加一些 Jenkins 的範例，希望這篇有幫助到你 !

# 結束，今天我們就將 Jenkins 架設完成囉

# 備註 - 沒有密碼時的步驟

## 查看 docker 目前執行的 container

```
# docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED         STATUS          PORTS                                                                                      NAMES
d9146583cb09   jenkins/jenkins:lts-jdk11   "/sbin/tini -- /usr/…"   4 minutes ago   Up 34 seconds   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp, 0.0.0.0:50000->50000/tcp, :::50000->50000/tcp   jenkins
```

## 進入 container

```
# docker exec -it d9146583cb09 /bin/bash

jenkins@d9146583cb09:/$ cat /var/jenkins_home/secrets/initialAdminPassword
61e8c8cb00c0417bb4c4719ba8559060
```

接下來就可以看到密碼囉， ```61e8c8cb00c0417bb4c4719ba8559060```

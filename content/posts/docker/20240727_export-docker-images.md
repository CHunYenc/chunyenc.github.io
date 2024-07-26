---
title: "Docker 紀錄 04 - 離線部署 Docker Image 時的指令"
description: "當網路不佳時，需要離線部署 Docker Image 時的指令。"
date: 2024-07-26T17:45:14Z
image: 
slug: "docker-export-docker-image"
categories:
    - Experience
    - Tutorial
tags:
    - GIT
    - Docker
    - Heroku
    - render
math: 
license: 
hidden: false
comments: true
draft: false
---

# 前言

因為公司網路系統上線的地方在中國，不管是 `docker`, `python` 套件都要更換下載源。

覺得麻煩，所以就下定決心使用離線部署。

以下使用 mysql 來做範例。

# 輸出 image

```sh
docker save mysql:8.0.30 > 240726_mysql.tar
```

結束後會產生一個檔案，用來儲存 image，然後你就可以把 `tar` 檔丟到系統上線的那台主機上。

## 壓縮，讓傳遞更快

因為 VPN 速度不佳，所以我們透過壓縮來減少檔案大小，加快傳輸速度。

我們使用 `zstd` 解壓縮演算法來進行壓縮。 (這邊就不特別介紹 zstd)

```sh
zstd -19 240726_mysql.tar
```

結束後會產生一個檔案，例如我的檔名會叫做 `240726_mysql.tar.zst`。

## 比較大小

這邊就用 `du` 來比較大小。

### 使用 zstd 解壓縮前

```sh
ubuntu@ubuntu70:/system/mes$ du -sh 240726_mysql.tar
440M    240726_mysql.tar
```

### 使用 zstd 解壓縮後

```sh
ubuntu@ubuntu70:/system/mes$ du -sh 240726_mysql.tar.zst
80M     240726_mysql.tar.zst
```

差超多 .. 又幫我節省很多時間了 XD

# 匯入 image

## 從 zstd 轉回 tar

```sh
# 使用 zstd 解壓縮成 tar
zstd -d 240726_python3.12-slim.tar.zst
# 使用 tar 匯入 docker 
docker load < 240726_mysql.tar 
```

## 從 tar 匯入 image

這個是最基礎的方式，如果你沒有使用 zstd 解壓縮，就直接使用。

```sh
docker load < 240726_mysql.tar
```

## 查看 image

```sh
docker images
```

# 參考資料

- [Docker 常用指令](https://docs.docker.com/engine/reference/commandline/save/)
- [Docker 常用指令](https://docs.docker.com/engine/reference/commandline/load/)
- [匯出/匯入 Docker image](https://bingdoal.github.io/deploy/2021/11/dokcer-import-export-to-file/)
- [zstd] (<https://github.com/facebook/zstd>)

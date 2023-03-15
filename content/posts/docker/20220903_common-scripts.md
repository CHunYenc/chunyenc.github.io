---
title: "Docker 紀錄 03 - 經常使用的 docker 指令"
description: 
date: 2022-09-03T12:55:54+08:00
slug: "docker-common-commands"
categories:
    - Experience
tags:
    - Docker
hidden: false
comments: true
draft: false
---

# 正文

## 建立 image

提供複製的指令。

```bash
# create image from dockerfile
docker build -t <image-name> . --no-cache
```

實際上在使用的時候，會是以下的範例。

```bash
docker build -t mydocker . --no-cache
```

輸入完後 docker image 就會開始建立。

完成後，進行檢查時就使用下面的指令。

```bash
docker images
```

然後就顯示機器上擁有的 docker images

```
REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
mydocker                 latest    0a045e9f442f   19 minutes ago   568MB
```

## 執行 image

```bash
docker run <image-name>
```

## 刪除 image

如何先查看本機上已經建立的 image 清單.

```bash
docker images
-
REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
mydocker                 latest    0a045e9f442f   19 minutes ago   568MB
```

```bash
# 這邊刪除上面建立的 image 
docker rmi 0a045e9f442f
```

# 範例

經常使用的 docker run 範本，所以導致本篇會持續更新的原因。

# postgres

## 好看版本

```
docker run -d \
--restart always \
--name dev-postgres \
-p 5432:5432 \
-e POSTGRES_PASSWORD=postgres \
-v /home/user/dev-pg-data/pgdata:/var/lib/postgresql/data \
--network dev-network postgres:10
```

## 複製版本

```
docker run -d --restart always --name dev-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -v /home/user/dev-pg-data/pgdata:/var/lib/postgresql/data --network dev-network postgres:10
```

# redis

## 好看版本

```
docker run -d \
--restart always \
-p 6379:6379 \
--name dev-redis \
--network dev-network redis
```

## 複製版本

```
docker run -d --restart always -p 6379:6379 --name dev-redis --network dev-network redis
```

# oracle-xe

## 好看版本

```
docker run -d \
--restart always \
--name dev-oracle -p 1521:1521 \
-e ORACLE_PASSWORD=<your password> \
-v oracle-volume:/u01/app/oracle/oradata gvenzl/oracle-xe:11
```

## 複製版本

```
docker run -d --restart always --name dev-oracle -p 1521:1521 -e ORACLE_PASSWORD=<your password> -v oracle-volume:/u01/app/oracle/oradata gvenzl/oracle-xe:11
```

# nginx

待補 

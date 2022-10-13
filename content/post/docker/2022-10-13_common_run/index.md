---
title: "Docker 紀錄 04 - 經常使用的 docker run"
description: "一直 Google 找別人的也好累, 來做一點自己常用執行的紀錄。"
date: 2022-10-13T20:21:30+08:00
slug: "common-docker-run"
image: docker.png
categories:
    - Experience
tags:
    - Docker
hidden: false
comments: true
draft: false
---

# 前言

這篇是自己常用的 docker run 指令，其他基本知識這邊不在補充了

其實可以透過 ```docker run --help``` 來看底下 ```-p```、```--name``` 等等的指令意思是什麼。

# postgres

```
docker run --restart always --name dev-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:10
```

# redis

```
docker run --restart always -p 6379:6379 --name dev-redis -d redis
```

# oracle-xe

```
docker run -d --restart always --name dev-oracle -p 1521:1521 -e ORACLE_PASSWORD=<your password> -v oracle-volume:/u01/app/oracle/oradata gvenzl/oracle-xe:11
```
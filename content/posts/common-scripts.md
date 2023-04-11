---
title: "置頂 - 提高效率的必備指令：一份我的常用指令與工具清單"
description: "工作時常使用到的指令與工具"
date: 2023-01-18T11:38:22+08:00
slug: "common-scripts"
categories:
    - Experience
tags:
    - GIT
    - Docker
    - VSCode
math: 
license: 
hidden: false
comments: true
draft: false
weight: 1
---

# 前言

主要為存放工作中經常使用的指令、框架、套件。

若有任何建議或是覺得需要修改的地方還請不吝指教，謝謝！

如何聯繫我 ?

> 可以利用本篇文章下面留言，導航列也有提供我的社群平台 ~

# 目錄

電腦版右側有目錄，手機版沒有，這邊的目錄為了手機版而整理 !

- [前言](#前言)
- [目錄](#目錄)
- [套件框架區](#套件框架區)
  - [VSCode](#vscode)
    - [Markdown](#markdown)
- [常用指令區](#常用指令區)
  - [Git](#git)
    - [下載子模組](#下載子模組)
    - [切換遠端分支](#切換遠端分支)
  - [Vue](#vue)
    - [更改 Port](#更改-port)
  - [Docker](#docker)
    - [Redis](#redis)
    - [PostgreSQL](#postgresql)


# 套件框架區

## VSCode

### Markdown

- https://github.com/yzhang-gh/vscode-markdown `自動生成 md 目錄` 

# 常用指令區

## Git

Git 是一個分散式版本控制系統，用於追蹤檔案變更並協助多人共同開發專案。

### 下載子模組

當你使用 git `clone` 下載完儲存庫後，發現沒有下載 submodule, 使用下面的指令可以直接把子模組載入。

```
git submodule update
```

### 切換遠端分支

`待補`


## Vue

### 更改 Port

`cli-services` 版本為 `@vue/cli-service": "~5.0.0`，如果不是也可以試試看。

```bash
# default 8080
npm run serve -- --port 8000
```
## Docker

### Redis

```
docker run -d \
--restart always \
-p 6379:6379 \
--name dev-redis \
--network dev-network redis
```

> Q: 為什麼有 dev-network ? 
>
> A: 為了可以讓開發容器可以直接使用 `dev-redis` 進行連線 ! 前提是開發容器也要使用 dev-network 建立 ! 

### PostgreSQL

```
docker run -d \
--restart always \
--name dev-postgres \
-p 5432:5432 \
-e POSTGRES_PASSWORD=postgres \
-v /home/user/dev-pg-data/pgdata:/var/lib/postgresql/data \
--network dev-network postgres:10
```
---
title: "Docker 紀錄 03 - 經常使用的 docker 指令 (持續更新)"
description: 
date: 2022-09-03T12:55:54+08:00
slug: "2022-docker-command"
categories:
    - Experience
tags:
    - Docker
hidden: false
comments: true
draft: false
---

# 前言

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
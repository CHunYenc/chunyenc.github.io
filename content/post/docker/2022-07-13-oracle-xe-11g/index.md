---
title: "2022 07 13 Oracle Xe 11g"
description: 
date: 2022-07-13T10:36:26+08:00
image: oracle.png
math: 
license: 
hidden: false
comments: true
draft: false
---

# 前言

主要紀錄建立 oracle-xe-11g 這個 image 的過程。

# 容器大小

```shell
root@vm-1-47:/home/ubuntu# docker images
REPOSITORY                        TAG        IMAGE ID       CREATED         SIZE
oracleinanutshell/oracle-xe-11g   latest     ad13c30ec346   3 years ago     2.13GB
```

# 操作

## docker

### docker run

```shell
docker run -d --name oracle-db -p 1521:1521 -e ORACLE_ALLOW_REMOTE=true oracleinanutshell/oracle-xe-11g
```

說明：

1. -d 為背景執行
2. --name
    - ```container-name```，把你的容器命名
3. -p 為 port 號
    - ```host-port:container-port```
4. -e 為環境變數
    - ```ORACLE_ALLOW_REMOTE```，因為要建立在虛擬機上，要從其他電腦連過來。

## oracle

### docker exec

執行之前，我們要先查看我們 oracle-db 的 CONTAINER ID

```shell
root@vm-1-47:/home/ubuntu# docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS        PORTS                                          NAMES
18681d31f0ec   oracleinanutshell/oracle-xe-11g   "/bin/sh -c '/usr/sb…"   3 seconds ago   Up 1 second   22/tcp, 8080/tcp, 0.0.0.0:1521->1521/tcp       oracle-db
```

這時候後複製 ```18681d31f0ec```。

```shell
root@vm-1-47:/home/ubuntu# docker exec -it 18681d31f0ec /bin/bash
root@18681d31f0ec:/#
```

## 建立 oracle user

```shell
root@18681d31f0ec:/# su - oracle
oracle@18681d31f0ec:~$ sqlplus / as sysdba

SQL*Plus: Release 11.2.0.2.0 Production on Wed Jul 13 03:04:33 2022

Copyright (c) 1982, 2011, Oracle.  All rights reserved.


Connected to:
Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production

SQL> create user yen identified by 0107;
User created.
SQL>
```

## 授予 oracle user 權限

```shell
SQL> grant dba to yen;
Grant succeeded.
```

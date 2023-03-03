---
title: "PSQL 01 - 踢掉指定的 PostgreSQL Session."
description: "強制取消後端測試時, 導致無法刪除已經建立的測試資料庫。"
date: 2023-03-03T06:11:52Z
slug: "psql-01"
categories:
  - Experience
tags:
  - Django
  - Python
hidden: false
comments: true
draft: false
---

# 前言

主要是在撰寫 Django 測試時，有時候會因為某些原因導致測試過程強制中斷，例如程式出錯或手動中斷執行等。

當發生這種情況時，測試資料庫可能會佔有一些 session 無法正確刪除，進而影響測試的正確性。

以下是發生的一些關鍵字或 .... 問題

```bash
(venv) user@vm:~/backend$ python manage.py test SomethingTestCase -v 3
Creating test database for alias 'default' ('test_template')...
Got an error creating the test database: database "test_template" already exists

Type 'yes' if you would like to try deleting the test database 'test_template', or 'no' to cancel: yes
Destroying old test database for alias 'default' ('test_template')...
Got an error recreating the test database: database "test_template" is being accessed by other users
DETAIL:  There is 1 other session using the database.
```

可以看到最後有出現一行關於 database session 的問題。

`DETAIL:  There is 1 other session using the database.`

# 如何解決

## 查詢目前在 PostgreSQL 中的 Session 有幾個 ?

當 PostgreSQL 資料庫中發現有用戶端連線時，就會產生一個會話或連線的記錄。

```sql
SELECT *
FROM pg_stat_activity;
```

使用此命令可以查詢正在執行的所有 SQL 語句、會話的狀態、用戶名、資料庫名、主機名、客戶端應用程式等資訊。

可用於診斷資料庫中的問題，例如瞭解目前資料庫是否被其他用戶連線、哪些查詢正在執行，以及為什麼某些查詢會長時間運行等。

### 範例

| datid | datname       | pid     | usesysid | username | application_name  | client_addr | query     | ... |
| ----- | ------------- | ------- | -------- | -------- | ----------------- | ----------- |  --------- | --- |
| 10000 | test_template | 2191385 | 10       | postgres | DBeaver 22.3.5... | 192.168.x.1   | select a .. |
| 19000 | template      | 2191386 | 10       | postgres | DBeaver 21...     | 192.168.x.2   | select b .. |

> 範例就是 pg_stat_activity 這張表會呈現的內容，資訊量非常豐富。

## 如何踢出指定的 Session ?

今天假設我要踢掉範例中的 pid 為 2191385 的 Session.　這時候只要打上下方的指令

```sql
SELECT pg_terminate_backend(2191385);
```

這時候你查詢 `SELECT * FROM pg_stat_activity;` 一次，你看一下你打上的 pid 對應的 session 是不是已經被你刪除了 !

## 那我要怎麼清楚某個指定 user 下的所有 session ?

這個查詢會返回所有用戶名等於 `username` 的 PostgreSQL Session。

```sql
SELECT * FROM pg_stat_activity WHERE usename = '<username>';
```

# 完成

今天是一個 PostgreSQL 的使用知識，正好在寫測時時出現，就把這個過程記錄一下。

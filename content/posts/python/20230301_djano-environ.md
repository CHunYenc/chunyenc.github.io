---
title: "Django 紀錄 03 - 使用套件 django-environ 管理環境參數 !! 超方便 !!"
description: "在工作時發現同事使用 .. 發現很好用 !! 所以有花時間研究一下。"
date: 2023-03-01T17:43:00+08:00
slug: "django-environ"
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

當今年二月不斷的補班的時候 ...　發現團隊內部有人使用 `django-environ` 套件。

筆者過去是使用 `python-dotenv`。但是發現 `django-environ` 有提供更多針對 `django` 框架的框架設定 !

- 讀取和解析環境檔案 (.env) 中的變數
- 將環境變數轉換成適當的 Python 型別
- 提供一些方便的方法來取得常用的設定值，如`資料庫連接字串`、`快取設定`、`郵件設定`等
- 支援多種格式的環境變數，如 JSON、YAML、INI 等

> 針對 `資料庫連接字串`、`快取設定` 就是一大優點

# 優勢 1 - 資料庫接字串

## 使用前的設定

筆者再使用 django-environ 前是使用 `python-dotenv`

```python
# settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql", # 1- 設定 ENGINE
        "NAME": variables.POSTGRESQL_NAME, # 2- 資料庫名稱
        "USER": variables.POSTGRESQL_USER, # 3- 資料庫使用者
        "PASSWORD": variables.POSTGRESQL_PASSWORD, # 4- 資料庫密碼
        "HOST": variables.POSTGRESQL_HOST, # 5- 資料庫 IP
        "PORT": variables.POSTGRESQL_PORT, # 6- 資料庫 PORT
    }
}
# variables.py 管理環境變數
POSTGRESQL_PASSWORD = os.getenv("DB_PASSWORD", "DEFAULT_PASSWORD") # 如果沒有 DB_PASSWORD, 就是 DEFAULT_PASSWORD
POSTGRESQL_HOST = os.getenv("DB_HOST", "localhost") # 如果沒有 DB_HOST, 就是 localhost
....
# .env
DB_PASSWORD = postgres 
POSTGRESQL_HOST = 192.168.1.1
....
```

通常我們使用 Django 去連接資料物的時候可能都會需要這些設定。

## 使用後的設定

筆者再使用 django-environ 後就直接縮短這個部分的參數

```python
# settings.py
DATABASES = {
    'default': variables.DATABASE
}
# variables.py
DATABASE = env.db()  # default load .env DATABASE_URL
# .env
DATABASE_URL="postgres://postgres:postgres@192.168.1.1:5432/mydb"
# 如果我要更換成 MYSQL
DATABASE_URL="postgres://postgres:postgres@192.168.1.1:5432/mydb"
```



# 優勢 2 - 快取設定

```
待補
```

# Reference
1. joke2k/django-environ: Django-environ allows you to utilize 12factor inspired environment variables to configure your Django application. - GitHub. https://github.com/joke2k/django-environ 已存取 2023/3/1.
2. 02. django-environ - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天. https://ithelp.ithome.com.tw/articles/10233649 已存取 2023/3/1.
3. Welcome to django-environ documentation - Read the Docs. https://django-environ.readthedocs.io/ 已存取 2023/3/1.
4. Django-environd的使用(管理配置文件敏感参数和环境变量)_想学废更多东西的猿的博客-CSDN博客_django environ. https://blog.csdn.net/zscccccc/article/details/121630824 已存取 2023/3/1.
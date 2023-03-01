---
title: "Django 紀錄 03 - 使用套件 django-environ 管理環境參數 !! 超方便 !!"
description: "在工作時發現同事使用 .. 發現很好用 !! 所以有花時間研究一下。"
date: 2023-03-01T17:43:00+08:00
slug: "2023-django-environ"
categories:
  - Experience
tags:
  - Django
  - Python
hidden: false
comments: true
draft: true
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

```
```

# 優勢 2 - 快取設定

```
```

# Reference
(1) joke2k/django-environ: Django-environ allows you to utilize 12factor inspired environment variables to configure your Django application. - GitHub. https://github.com/joke2k/django-environ 已存取 2023/3/1.
(2) 02. django-environ - iT 邦幫忙::一起幫忙解決難題，拯救 IT 人的一天. https://ithelp.ithome.com.tw/articles/10233649 已存取 2023/3/1.
(3) Welcome to django-environ documentation - Read the Docs. https://django-environ.readthedocs.io/ 已存取 2023/3/1.
(4) Django-environd的使用(管理配置文件敏感参数和环境变量)_想学废更多东西的猿的博客-CSDN博客_django environ. https://blog.csdn.net/zscccccc/article/details/121630824 已存取 2023/3/1.
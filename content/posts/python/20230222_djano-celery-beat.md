---
title: "Django 紀錄 02 - 如何在 Django 應用使用 Celery 進行系統任務管理"
description: "雖然 Djang 也有其他的任務套件, 但 Celery 用起來還是問題最少 .."
date: 2023-02-22T22:17:10+08:00
slug: "2023-django-celery-beat"
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

最近在使用 `django-celery-beat`，發現網路上的參數基本上都舊了。

所以安裝的方式這邊幫大家梳理一下，有時候網路上的安裝方式可能會導致自己花非常多時間。

> 如果你是老手，可以直接到 Github 查看程式碼。

https://github.com/CHunYenc/django-celery-beat-example

# 版本

python 3.10.7
django 4.1.7
celery 5.2.7
django-celery-beat 2.4.0

# 步驟

## 建立虛擬環境

為了讓專案有個乾淨的環境, 必須建立虛擬環境 !!

### Linux / Mac

```shell
python -m venv .venv
```

### Windows

```shell
py -3.10 -m venv .venv
```

## 進入虛擬環境

### Linux / Mac

```shell
source .venv/bin/activate
# 進入後
(.venv) path % ... 
```

### Windows

```shell
.venv\Scripts\Activate.ps1
# 進入後
(.venv) PS > ...
```

## 安裝套件

```
```

## 建立 Django Project

這邊筆者的路徑是已經在 `/Users/yen/code/django-celery-beat-example`，

所以當你使用下列指令時，你的 `core` 資料夾位置應該會是 `/Users/yen/code/django-celery-beat-example/core`

```shell
# (.venv) django-celery-beat-example % 
django-admin startproject core .
```

## 安裝 Django-Celery-beat

### core/settings.py 的 INSTALLED_APPS

安裝 `django-celery-beat` 在 `INSTALLED_APPS`。

```python3
# 開發時的習慣, 上線建議不要使用 *
ALLOWED_HOSTS = ['*']

# 主要內容 INSTALLED_APPS 加入 'django_celery_beat'
INSTALLED_APPS = [
    ...
    ...
    ...
    # packages
    'django_celery_beat',
]
```

安裝上去會發現，`django-celery-beat` 有預設的資料表來控制任務喔 !!!

### core/settings.py

當 django-celery-beat 啟動時, 會先讓 celery 讀取 django settings。

```python3
# CELERY STUFF
CELERY_BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_TIMEZONE = "UTC"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_IMPORTS = ["core.tasks"] # 任務的程式碼檔案
CELERY_BEAT_SCHEDULE = {
    "system-task": {
        "task": "system-get-pricing",
        "schedule": 10.0
    }
}
```

### core/celery.py

```

```
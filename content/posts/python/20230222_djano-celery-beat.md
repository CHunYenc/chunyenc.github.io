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

| name                   | version |
| ---------------------- | ------- |
| **python**             | 3.10.7  |
| **django**             | 4.1.7   |
| **celery**             | 5.2.7   |
| **django-celery-beat** | 2.4.0   |

# 步驟

## 建立虛擬環境

當使用 Python 時會使用到大量套件或不同版本的 Python 時，建立虛擬環境可以幫助隔離 Python 的不同版本和套件，以避免版本衝突。

> 為了讓有乾淨的環境, 必須建立虛擬環境 !!

### Linux / Mac

```shell
python -m venv .venv
```

### Windows

```shell
py -3.10 -m venv .venv
```

## 進入虛擬環境

接下來啟動 Python 虛擬環境，執行後你的 shell 會切換到虛擬環境中。

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

> 下面我就僅使用 (.venv) 表示虛擬環境。後面會直接接指令。

## 安裝套件

```
(.venv) pip install django celery[redis] django-celery-beat
```

## 建立 Django Project

這邊筆者的路徑是已經在 `/Users/yen/code/django-celery-beat-example`，

所以當你使用下列指令時，你的 `core` 資料夾位置應該會是 `/Users/yen/code/django-celery-beat-example/core`

```shell
(.venv) django-admin startproject core .
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

### core/celery.py

在這個檔案中設定 Celery 的 instance。一般會設定 broker 和 backend 的位置，以及指定 task 檔案的位置等等。有了這個設定之後，Django 就能夠將要執行的 task 發送到 Celery，由 Celery 負責執行。

```python3
import logging
import os
from kombu import Exchange, Queue

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# 建立一個 Celery 實例，名稱為 core
app = Celery('core')

# 設置 broker 和 backend
app.conf.broker_url = "redis://localhost:11855/1"
app.conf.result_backend = "redis://localhost:11855/0"

# 設置時區和序列化方式
app.conf.timezone = "UTC"
app.conf.accept_content = ['application/json']
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'json'
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

# 設置要被 celery worker 載入的任務模組
app.conf.imports = ["core.tasks"]

# 設置定時任務
app.conf.beat_schedule = {
    "system-task": {　# Celery 任務名稱
        "task": "system-hello-celery", # Celery 任務執行的函示名稱
        "schedule": 2.0 # 每兩秒執行一次
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

logger = logging.getLogger('django.celery')
```

`broker_url`: Celery 的`消息中介`。主要 `來處理任務的分發和調度`，因為它可以將分散在各個系統之間的工作協調起來。

`result_backend`: Celery 結果儲存位置。

`timezone`: Celery 的時區。

`accept_content`: Celery Worker 接受的任務格式。除了 `json` 外, 還有 `pickle` 等等的任務結構。 

`task_serializer`: Celery Worker 執行任務(程式)時需要進行序列化以方便傳輸和儲存。這邊使用 `json`。

`result_serializer`: Celery Worker 完成任務(程式)時需要進行序列化儲存至 `RESULT_BACKEND` 指定的 `redis`。這邊也是使用 `json`。

`imports`: 你可以使用 `["core.tasks", "app.tasks.function"]` 來導入你的任務程式。

`beat_schedule`: 是 Celery 預設的調度器，是後端啟動時直接啟用。

> SERIALIZER 為什麼要設定呢 ? 因為 Celery 4.0 之前是使用 pickle.

其他我沒提到的設定參數可以到下面連結查看。

https://docs.celeryproject.org/en/stable/userguide/configuration.html#configuration-reference


### core/__init__.py

在 `__init__.py` 主要是要讓 Django 項目中使用 `celery_app` 與 `celery_logger` 物件。

```python3
# core/__init__.py
from __future__ import absolute_import
from core.celery import app as celery_app, logger as celery_logger

__all__ = ('celery_app', 'celery_logger',)
```

### core/tasks.py

主要將 Celery 要執行的程式寫在此處。而 Celery 就會登入該檔案的函式。

例如這邊有一個 Celery 函示叫 `system-hello-celery`, 就是對應 `core/celery.py` 中的 `beat_schedule` 內的 task。

```python3
import json
from core import celery_logger
from celery import shared_task

@shared_task(name="system-hello-celery")
def hello_celery():
    celery_logger.info("HELLO Celery")
```

## 執行 Celery

### 使用 Docker 建立 redis

```shell
docker run -d --restart always -p 6379:6379 --name dev-redis redis
```

> 如果在本機執行 docker, 那麼 IP 就是 `localhost:6379`。

### migrate database

當您在 Django 中更改模型之後，例如添加、修改或刪除模型，您需要將這些變更反映到資料庫中。

```
(.venv) python manage.py migrate
```

### run celery

#### 開發用

```shell
(.venv) celery -A core.celery worker -l info -B
``` 

#### 上線時 (production)

在正式環境中，不建議在同一個應用程序中運行 worker 和 beat scheduler，因為會影響應用程序的性能和穩定性。

##### 第一個 terminal

```shell
(.venv) celery -A core.celery worker --loglevel=info
```

##### 第二個 terminal

```shell
(.venv) celery -A core.celery beat -l info
```

> 你也可以使用 docker-compose 執行個別一個 services。
# 完成 

```shell
... 省略
[2023-02-24 09:47:46,349: INFO/MainProcess] celery@DESKTOP-7GLUFOT ready.
[2023-02-24 09:47:46,359: INFO/MainProcess] Task system-hello-celery[409aa851-639d-4183-92eb-662715a55b41] received
HELLO Celery
[2023-02-24 09:47:46,361: INFO/ForkPoolWorker-2] HELLO Celery
[2023-02-24 09:47:46,381: INFO/ForkPoolWorker-2] Task system-hello-celery[409aa851-639d-4183-92eb-662715a55b41] succeeded in 0.02016970000022411s: None
```

# 後續

你還可以透過 `django-environ` 套件來優化你的 `settings.py` 或 `celery.py`，將環境設定的資訊都隱藏。

那也是我後續要來新增的文章 XD
---
title: "20221117_Flask-Caching 套件來使用 redis."
description: "Flask 上下文導致 redis 引入一直有問題, 所以改用 Flask-Caching, 但是 ..."
date: 2022-11-17T22:57:28+08:00
image: "flask.png"
slug: "flask-01"
categories:
  - Experience
tags:
  - Flask
  - Python
hidden: false
comments: true
draft: false
---

# 簡介

主要在 Flask 連接 redis 一直發生問題，所以使用 ```Flask-Caching``` 來處理讀寫 redis.

但是還是有一點問題，就是 ```Flask-Caching``` 官方沒有支援讀取 redis 的用法，但是在網路上有看到一則留言。

成功所以紀錄一下。

> 程式碼在此 [Github - CHunYenc/crypto-price-scheduler](https://github.com/CHunYenc/crypto-price-scheduler/tree/01567cdf781025f01167f35ad649b4f0f0ea493c)

> Flask-Cacing 文檔 [Flask-Caching docs](https://flask-caching.readthedocs.io/en/latest/) 

# 安裝 Flask-Caching

```
pip install Flask-Caching
```

# Init Flask-Caching

```python3
from flask_caching import Cache

cache = Cache(config={"CACHE_TYPE": "RedisCache"})

def create_app(env):
    ...
    app = Flask(__name__)
    app.config.from_object(config[env])
    ...

    with app.app_context():
        ...
        # Caching
        cache.init_app(app)
        ...
```

# 讀 redis 特殊方式

```python3
k_prefix = cache.cache.key_prefix
keys = cache.cache._write_client.keys(k_prefix + "*")
keys = [k.decode("utf8") for k in keys]
keys = [k.replace(k_prefix, "") for k in keys]
```

k_prefix 是 Flask-Caching 會自動加入 flask-cache 在 redis 上面，所以需要把 k_prefix 去除。

> 程式碼參考位置 /backend/app/socket.py

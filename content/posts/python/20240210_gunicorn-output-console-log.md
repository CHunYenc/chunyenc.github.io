---
title: "Gunicorn - 輸出 Console Log, 在 Railway."
description: "在 Railway 上使用 Gunicorn 時，如何輸出 Console Log，不然沒辦法知道系統的運行狀況。"
date: 2024-02-10T00:20:00+08:00
slug: "gunicorn-output-console-log"
categories:
  - Experience
tags:
  - Python
hidden: false
comments: true
draft: false
---

# 前言

這篇的產出主要是因為我自己在使用 Railway.app (Paas 平台) 的時候，發現沒有辦法看到 Gunicorn 的 Console Log ... 如果系統有問題，我根本不知道發生了什麼事情。

因為筆者過去都使用 Docker Compose + Gunicorn 或是有需要就接到 Nginx (or Apache) 的架構，所以都是直接看 Log。

甚至 Gunicorn 也可以設定輸出到檔案，然後透過 `tail -f` 來觀看。

但是本次是在 Railway.app 上，所以就有這篇的產出。

# 最終設定

在 Railway.app 上，我們可以透過設定 `Custom Start Command` 來達到我們的目的。

```bash
gunicorn --access-logfile '-' --error-logfile '-' app:app
```

這樣就可以把 Console Log 輸出到標準輸出 (stdout) 了。

# 結論

其實非常簡單, 但是我花了一些時間才找到這個設定。

而且現在大家都靠 GPT-3 了，所以我也不知道這篇文章有沒有人會看到 XDDD

希望這篇對你有幫助。

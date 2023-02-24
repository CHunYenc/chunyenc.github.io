---
title: "教學 - 如何讓 render.com 提供的機器不睡眠"
description: "使用 heroku、render.com 等平台的免費機器，基本上都會自動睡眠."
date: 2023-01-27T15:53:22+08:00
image: 
slug: "wakup-machine"
categories:
    - Experience
tags:
    - GIT
    - Docker
    - Heroku
    - render
math: 
license: 
hidden: false
comments: true
draft: false
---

# 前言

> 祝大家新年快樂 !!!

今天是初六，也休息一陣子了，覺得有點廢。

主要是因為大四時擔任宿舍網路會長時製作的 LINE-BOT 上線在 `heroku`，但是 `2022/12` 已經公告說他們要開始收錢了。於是我就將 LINE-BOT 的伺服器轉移到 `render.com` 平台。

那在轉移時有製作一個工具。就是要不間斷的去呼叫免費平台(類似 heroku.com、render.com)。

> 就是要讓機器永遠不睡眠 ! 操爆它 (X)

統整做了三件事：
1. 運用 Python 定時呼叫小應用的網址
2. 利用 Docker 彈性系統參數 
3. 利用 Docker Compose 定時呼叫多個平台

本篇不是教你怎麼做這個工具，是教你如何用。

所以會從 `2.` 來教你怎麼做 !

<!-- # 使用 Python 來製作我們的工具

呼應 `1.` 透過 `Python` 來製作我們的工具。

> 如果你是想知道怎麼使用這個 `Image` 建議你從下一節 (`使用 Docker 來把工具包裝起來`) 看起 ~

程式碼連結：https://github.com/CHunYenc/wakeup-machine

有三個比較重要的檔案：
1. requirements.txt
   - 使用到的套件列表，使用指令 `pip install -r requirements.txt` 可以下載。 
2. variables.py
   - 使用到的環境變數列表。
3. app.py
   - 主要執行的程式碼
   - 其實才 5x 行 ..

> 開發模式下，要如何引入 variables.py 的變數呢？

# .env 與 variables.py

.env 是開發模式下需要引入的檔案。 `為了取代環境變數。`

`.env` 檔案就建立在 `app.py` 同一層。

## 範例

是一個範例，你可以複製拿去用。

```env
# .env
URL = https://chunyen.xyz # 呼叫的網址
APSCHEDULER_DAY_OF_WEEK = mon-fri # 禮拜一到五執行
APSCHEDULER_HOUR = 0-1,5-23 # 0-1, 5-23 點執行
APSCHEDULER_MINUTE = */10 # 每十分鐘執行

# APSCHEDULER_YEAR = ?? # 範例不使用, 但你可以用
# APSCHEDULER_MONTH = ?? # 範例不使用, 但你可以用
# APSCHEDULER_DAY = ?? # 範例不使用, 但你可以用
# APSCHEDULER_WEEK = ?? # 範例不使用, 但你可以用
# APSCHEDULER_SECOND = ?? # 範例不使用, 但你可以用
```

所以上面設定的參數意思為：

`週一到週五，每天五點到隔日一點的每十分鐘執行一次。`

> 你有發現變數名稱是對應 variables.py 中每一行 `os.getenv` 的第一個參數名稱嗎？

# app.py

```python
# app.py
def scheduled_job():
    """ 主要執行呼叫的 function """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    url = variables.URL
    req = request.Request(url=url, headers=headers)
    try:
        request.urlopen(req).read()
    except Exception as e:
        logging.info(f"{e}")
    else:
        logging.info(f"Successful connection {url}.")
``` -->

# 利用 Docker 來使用工具

`工具只需要透過 Docker 就可以執行囉 !`

範例如下：`範例下方還有部分說明唷 !`

`**** 記得要先建立一個 schedule.log 檔案。`

```shell
docker run -d \
--restart always \
--name wakeup-render \
-e URL=https://yourwebsite.domain.com/ \
-e APSCHEDULER_DAY_OF_WEEK=mon-fri \
-e APSCHEDULER_MINUTE=*/10 \
-v /Users/yen/Desktop/schedule.log:/app/scheduler.log \
chunyenc/wakeup-machine
```

- `--restart` 若重開機將自動執行
- `--name` container 的名稱
- `-e` 環境變數
  - URL 是你要呼叫的網址
  - APSCHEDULER_DAY_OF_WEEK 一週裡面哪幾天執行
  - APSCHEDULER_MINUTE 是多少分鐘呼叫一次
- `-v` 映射檔案
  - linux 可以使用 `pwd` 指令來查看目前的絕對路徑
  - schedule.log 就是查看執行 log 的檔案

## 環境變數列表

| 環境變數                | 範例值              | 備註                     |
| ----------------------- | ------------------- | ------------------------ |
| URL                     | https://chunyen.xyz | 呼叫的網址               |
| APSCHEDULER_YEAR        |                     |                          |
| APSCHEDULER_MONTH       |                     |                          |
| APSCHEDULER_DAY         |                     |                          |
| APSCHEDULER_WEEK        |                     |                          |
| APSCHEDULER_DAY_OF_WEEK | mon-fri             | 依照範例，設定週一到週五 |
| APSCHEDULER_HOUR        |                     |                          |
| APSCHEDULER_MINUTE      | */10                | 依照範例，設定每十分鐘   |
| APSCHEDULER_SECOND      |                     |                          |

> APSCHEDULER 需要參考下面網址來設定
> https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html


# 如果是使用 Docker Compose ..

```yaml
version: '3.9'

services:
  service-one:
    image: chunyenc/wakeup-machine
    environment:
      - URL=https://one.chunyen.xyz
      - APSCHEDULER_MINUTE=*/10
      - APSCHEDULER_HOUR=0-1,5-23
      - APSCHEDULER_DAY_OF_WEEK=mon-fri
    volumes:
      - ./pricing.log:/app/scheduler.log

  service-two:
    image: chunyenc/wakeup-machine
    environment:
      - URL=https://two.chunyen.xyz
      - APSCHEDULER_MINUTE=*/10
      - APSCHEDULER_HOUR=9-23
    volumes:
      - ./linebot.log:/app/scheduler.log
```
---
title: "我的第一篇 HUGO 架設 BLOG 經驗分享"
description: "沒什麼描述，就是講講這個部落格的產生原因"
date: "2022-03-26 20:46:00+0800"
slug: "hugo-blog-online"
image: "featured.png"
categories:
    - Hugo
tags:
    - Hugo
comments: False
---


# 更換成 Hugo 的原因

自己本身是有使用 Blogger，主要認為有下面幾個問題。

1. 垃圾留言
2. 介面很醜
3. 發文介面使用不易
   - 每次發文之後都會跑版，所以果斷使用一個自己架設的。
   - 不想一直預覽切來切去。
4. 不能使用 markdown 方式來撰寫你想要的文章 ***

# 更換過程

我認為官方的文件講得很清楚，我也是照者下面的連結馬上建立一個 quickstart 資料夾。

https://gohugo.io/getting-started/quick-start/

然後使用一個官方預設的 Theme (佈景主題?)

但我自己設定時候講想說「好醜」、「這什麼鬼主題」XD

所以現在看到的這個主題呢，是從官方(下面連結)找到的。

https://themes.gohugo.io/

# 我選的背景主題

https://themes.gohugo.io/themes/hugo-theme-stack/

底下有中文文檔，不過我還是中英文互相看，英文的文件我認為比較新。

建議可以直接看英文啦，反正就看一下 ```config.yml``` 怎麼設定。

```
config.yml 底下有檔案連結可以過去參考看看。
```

# 架設環境

主要有三個地方需要注意，以下是說明。

Reference 都有我參考的文章，關於 Reference 第 2 點的參考文章建立的 main.yml 是無法執行的。(我的 branch(gh-pages) 一直沒有建立出 HTML)

1. .github/workflows/main.yml
   - 檔案連結： https://github.com/CHunYenc/chunyenc.github.io/blob/master/.github/workflows/main.yml

2. config.yml
   - 檔案連結： https://github.com/CHunYenc/chunyenc.github.io/blob/master/config.yml
   - 在 config.yml 加入 publishDir: docs, 可以讓你每次下 ```hugo -t stack``` 都能夠生成 HTML 檔案到 docs 資料夾, 預設是到 public 資料夾

3. docs/

```
如果你有看到 Reference 第 1 點的參考文章使用兩個 repository, 
一個是主要去紀錄尚未生成的檔案, 
一個是生成的靜態檔案(就是指 HTML 放的位置)。

但是我不用，我只需要一個 repository !!!
```

以下是我準備將網站上線的過程，但是要注意你的上面前兩點都已經設定好 💪

👉 請確定已經將文章內容打好並且儲存後再執行

👉 請確定已經將文章內容打好並且儲存後再執行。

👉 請確定已經將文章內容打好並且儲存後再執行

```
hugo -t stack 
# 這時候會發現我們的 docs 資料夾內會有很多靜態檔案

git add .
git commit -m "feat: ..."
git push
```

這樣你等一下就可以在你的網頁上看到了！

# Reference

1. https://medium.com/@chswei/%E5%9C%A8-github-%E9%83%A8%E7%BD%B2-hugo-%E9%9D%9C%E6%85%8B%E7%B6%B2%E7%AB%99-9c40682dfe40
2. https://yurepo.tw/2021/03/%E5%A6%82%E4%BD%95%E5%B0%87hugo%E9%83%A8%E8%90%BD%E6%A0%BC%E9%83%A8%E7%BD%B2%E5%88%B0github%E4%B8%8A/
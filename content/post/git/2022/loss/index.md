---
title: "Loss"
description: 
date: 2022-07-06T17:59:19+08:00
image: 
categories:
    - GIT
tags:
    - git
hidden: false
comments: True
draft: false
---


# 前言

有一天下午，把某項任務完成後，就下指令 ```git add``` 

然後沒有 ```git commit``` ... (更不用說 ```git push```)

總之就在整理前後端版本對應的問題，然後就直接 ``` git checkout -f master ``` 跳去 master，主要是覆蓋版本，因為主分支已經很久沒有上新版了。

最後 ... 前端的程式碼被我弄丟了 !

# 解法

## git fsck

有看到一個 十年前的文章 (今天是 2022/07/07)

連結：http://blog.hsatac.net/2012/07/git-restore-removed-files/

```
PS C:\code\frontend> git fsck --cache --unreachable
Checking object directories: 100% (256/256), done.
Checking objects: 100% (2592/2592), done.
unreachable blob 7fc292a549c604ee4219b2e0db9383b32f3ce152
unreachable blob 05037508dd7dda94f5fb422a7867471247283403
unreachable blob 7c83ff9c66bf28827bd0fbb2aa5e377e460829fe
... 底下還有很多
```

接下來每行  ``` blob 7fc292a549c604ee4219b2e0db9383b32f3ce152 ``` 都是你之前尚未 commit 的檔案。(不是很確定

## git show 

接下來就是每一行的看檔案了 ...

```
git show 7fc292a549c604ee4219b2e0db9383b32f3ce152 > temp.txt
```

接下來你的 ``` C:\code\frontend ``` (這是我的位置)

就會看到有一個 ``` temp.txt ```

基本上就是檔案回來囉 ! 

希望對您有幫助 !

#完成
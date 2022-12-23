---
title: "GIT 小撇步 02 - 教你如何刪除 commit 過的大檔案, 超占空間 !"
description: "因為在準備 CI/CD 要減少每個步驟的耗費的時間，導致要整理 git .."
date: 2022-12-21T13:36:01+08:00
slug:
categories:
    - Experience
tags:
    - GIT
hidden: false
comments: True
draft: false
---

# 前言

準備要幫自己手上的專案套上 CI/CD，但是發現過去的資料其實沒有使用 ```submodule``` 的方式去管理 ```data```。

> 此處的 ```data``` 是一個資料夾，裡面放的是客戶系統的資料。會有 ```.csv``` or ```.json``` 的檔案。

所以導致系統的 ```儲存庫 (repository)``` 異常的大，都是大在過去 commit 過的紀錄。

> 最新的 commit 已經把所謂 ```data``` 的資料夾刪除了，但是 git 其實還會幫你存在 ```.git``` 資料夾

# 參考文章

> 感謝這邊的文章，雖然我還是卡一陣子，導致這篇文的產生 XD

## [CSDN - 彻底删除git中的较大文件（包括历史提交记录）](https://blog.csdn.net/HappyRocking/article/details/89313501)

## [高見龍 - 為你自己學 Git](https://gitbook.tw/chapters/faq/remove-sensitive-data)

## [Nils Jonsson - Rebasing tags in Git repositories](https://blog.nilsjonsson.com/post/4421450571/rebasing-tags-in-git-repositories)

# 先說結論

尚未優化前，佔 ```1.2G```

優化後，佔 ```121MiB```

# 步驟

## 建議執行前 fork 一份

可以在本地端或伺服器端。

local 端

- 做錯的話你可以直接 copy 重新
- 不用一直 clone

remote 端

- 主要是備份 .. 東西不見太恐怖了 !!!

> 請確實做好備份。

## 重新 clone 一次 (重新下載你的程式碼)

```shell
git clone https://..... project
```

我這邊範例將下載的資料夾取為 ```project```

這個動作是為了確保你本地端的程式碼與伺服器端的程式碼相同。

> 因為我們主要要解決儲存庫的　```.git```　資料夾。

## 查看 10 個在 Git 裡面最大的檔案

先假設 10 個檔案就可以找到我們心目中想要刪掉的檔案名稱，那為什麼我都使用 ```git rm```　的指令，

```shell
git rev-list --all | xargs -rL1 git ls-tree -r --long | sort -uk3 | sort -rnk4 | head -10
```

## 刪除 Git 檔案

提供你複製，複製後將 ```檔案名稱``` 更改掉，因為他要打上你想要刪除的檔案 or 資料夾。

```shell
git filter-branch --force --index-filter 'git rm -rf --cached --ignore-unmatch 檔案名稱' --prune-empty --tag-name-filter cat -- --all
```

下面是我的範例，提供給你參考。

```
# example 刪除 data folder, csv and json file.
git filter-branch --force --index-filter 'git rm -rf --cached --ignore-unmatch data *.json *.csv' --prune-empty --tag-name-filter cat -- --all
```

- ```*.json``` ：刪除 ```.json``` 檔名的檔案。
- ```--forec``` ：強制刪除
- ```--index-filter``` ：刪除的時候索引重寫。
- ```--prune-empty```：將空白的 commit 刪除。
- ```--tag-name-filter tag```: 將會重寫 tag 的索引。

Git 官方網站：[filter-branch](https://git-scm.com/docs/git-filter-branch)

# 清理 .git 資料夾

```shell
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now
git gc --aggressive --prune=now
git push origin master --force
```

這邊我有先將伺服器端的儲存庫刪除，再重新上傳。

> 注意要備份啊 !!!!!!

另外你也可以透過下面的指令看現在 .git 或 資料夾內部的使用空間。

```shell
cd project

# 查看 git 資料夾的使用空間
du -sh .git

# 查看全部檔案的使用空間, 但看不到 .git
du -sh * 
```
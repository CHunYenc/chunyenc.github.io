---
title: "GIT 小撇步 03 - Submodule 後的 git clone --recursive 下載指令"
description: "因為在準備 CI/CD 要減少每個步驟的耗費的時間，導致要整理 git .."
date: 2025-06-24T09:36:01+08:00
slug: "git-submodule-download"
categories:
    - Experience
tags:
    - GIT
hidden: false
comments: True
draft: false
---

# 前言

因為自己在專案上都使用 ```submodule``` 的方式去管理 ```子系統```

例如說一個系統會有

- ```frontend```
- ```backend```
- ```database```
- ```nginx```
- ```redis```
- ```logger```
- ```conf``` 雜七雜八的子系統, 甚至 docker 的設定檔案

所以這時候在 `移機` 或是 `fork` 套到子公司或是其他部門的時候可以更快速的移動整個系統

我是一直都認為這個方式很好管理系統，甚至可以在交接時可以快速的交接。

# 前置作業

你必須要透過 git submodule add 的方式去新增其他 repository 至你的 repository 中。

舉個例子：

當我有一個資料夾叫做 main-system，

這時候我要加入 frontend 的 repository，

```shell
# ./main-system
git submodule add https://your.com.tw/user/frontend.git frontend
git commit -m "add frontend submodule"
git push origin main
```

這樣你就可以在 github 上的 main-system 資料夾下找到 frontend 資料夾，

# 正式作業

你在 github 上可能已經看到 frontend 資料夾，

後面還會根據你 push 時的 frontend repository 的 commit id

直接鎖定版本，直接幫你做好此版本的版本管理。

但是我們在未來的 clone 都要加上 `--recursive` 的方式去 clone

否則會少掉 frontend 資料夾

```shell
git clone --recursive https://your.com.tw/user/main-system.git
```

這樣你就可以在 main-system 資料夾下找到 frontend 資料夾


# 如果不幸 clone 時沒有加上 --recursive

```shell
# ./main-system
git submodule update --init --recursive
```

這樣你就可以在 main-system 資料夾下找到 frontend 資料夾
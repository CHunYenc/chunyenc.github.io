# chunyenc.github.io

[![Build Status](http://drone.chunyen.xyz/api/badges/CHunYenc/chunyenc.github.io/status.svg?ref=refs/heads/master)](http://drone.chunyen.xyz/CHunYenc/chunyenc.github.io)

使用 hugo 建立的部落格網站。

- [chunyenc.github.io](#chunyencgithubio)
- [常用操作](#常用操作)
  - [Download](#download)
    - [best](#best)
    - [clone themes](#clone-themes)
  - [加入文章](#加入文章)
  - [發布](#發布)

# 常用操作

## Download

如果使用一般的 clone 方式，會導致沒有主題。

如果發現沒有主題，你可以參考 [clone themes](#clone-themes)

### best

```shell
git clone --recurse-submodules https://github.com/CHunYenc/chunyenc.github.io.git blog
```

### clone themes

```shell
git clone https://github.com/CHunYenc/chunyenc.github.io.git blog
cd blog
git submodule update
```

## 加入文章

```bash
hugo new post/folder/file.md
```

## 發布

```bash
hugo -t stack 
git add .
git commit -m "feat: ..."
git push
```

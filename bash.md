# 常用指令記錄

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
hugo -t hugo-theme-stack 
git add .
git commit -m "feat: ..."
git push
```

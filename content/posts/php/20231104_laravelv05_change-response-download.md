---
title: "Laravel(v5) - 更改 Response Download PDF 到直接打開 PDF"
description: "碰到 Laravel v5.x 還沒有 response()->file() 所以紀錄一下解決方式"
date: 2023-11-03T18:50:00Z
slug: "laravelv05-change-response-download"
categories:
    - Experience
tags:
    - PHP
    - Laravel
hidden: false
comments: true
draft: false
---

# 前言

公司官網使用 `Laravel v5.1.x`, 有一個功能是要讓使用者可以下載 PDF 檔案，但是原本的寫法是使用 `response()->download()`，但是這樣會導致使用者下載後還要再去開啟 PDF 檔案，所以要改成直接開啟 PDF 檔案。

但是我一開始發現 `laravel v10.x`, 有 `response()->file()` 可以使用，但是 `laravel v5.x` 沒有，所以要另外找方法。

## 流程

簡單來說操作流程如下, 因為主要在改善使用者瀏覽 PDF 或下載檔案的流程。

### 改善前

```mermaid
flowchart LR
    step1["點擊下載按鈕"]
    step2["等待下載 PDF 檔案
    (瀏覽器跳出下載視窗)"]
    step3["開啟 PDF 檔案
    (使用者自行開啟)"]
    step1 --> step2 --> step3
```

可以發現說, 使用者需要等待下載 PDF 檔案, 然後再去開啟(手動) PDF 檔案。

### 改善後

```mermaid
flowchart LR
    step1["點擊下載按鈕"]
    step2["等待開啟 PDF 檔案
    (瀏覽器直接開啟 PDF 檔案)"]
    step1 --> step2
```

這樣中間就會少一個步驟, 讓使用者可以直接開啟 PDF 檔案。

## 更改程式碼前

因為公司是使用 `Laravel v5.1.x`, 所以我們要去找到原本的程式碼在哪裡。

```php
# download.blade.php
<td>
    @if(!empty($value2['file']))
        <a href="{{ xx::url('download/'.$value2['id'].'?time='.time())}}"><img
                    src="../../assets/images/icons/icon-pdf.png" alt=""
                    class="icon-pdf"></a>
    @endif
</td>
```

從上面的 HTML 可以知道, 下載的路徑是 `download/{id}`。

然後還有搭配一個 Icon, 這邊就不多做介紹。

```php
....
# download/{id}
return response()->download($file_path, $file_name);
....
```

這邊就是原本的下載 PDF 檔案的程式碼, 這邊就是會直接透過瀏覽器下載 PDF 檔案。

## 有趣的事情

因為透過 PDF 直接打開後，會發現到每次開啟檔案都不是 PDF 檔名了。而是 PDF 文件標題，而公司文件的標題非常的亂 ... 甚至還有一些奇怪的符號、COPY 其他公司的文件來改的 .. 所以後面我又寫了一隻 Python 程式來幫我把全部 PDF 檔案的標題改掉。

至於 PHP 能不能夠改 PDF 的檔案標題，我沒有找到方法，所以就用 Python 來做了。

如果你是用 PHP 的話，也歡迎你跟我說你用什麼套件來改 PDF 檔案標題。

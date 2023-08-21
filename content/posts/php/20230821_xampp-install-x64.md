---
title: "Php - XAMPP x64 安裝 Oracle Instant Client"
description: "公司使用 x64 的OCI8一直沒成功，這邊算是紀錄解決的關鍵點"
date: 2023-08-21T07:41:54Z
slug: "xampp-x64-oracle-instant-client"
categories:
    - Experience
tags:
    - Oracle
    - PHP
    - Database
hidden: false
comments: true
draft: false
---

# 前言

近期換了工作，而這份工作是使用原生 PHP。有預計會升級為 `Laravel`。

那在安裝 PHP 開發過程中，遇到一個令人挑戰的問題。公司前輩沒有使用 XAMPP x64 環境下成功安裝 OCI8。主要還是我`自發性`去解決這個問題。主要我覺得很簡單，但是中間還是碰到一些問題，所以才會留下這篇文章。

所以到我解決這件事情前，公司到目前上線的系統都是使用 x32 架構的 OCI8。接下來還要把上線的系統改為 `x64`，所以接下來有得忙了 XD

希望這篇文章能為那些正在尋找解決方案的人們提供一些有價值的指引，幫助大家節省時間和精力。

# 關鍵

主要系統為 `Windows`，若要使用 `Linux` 可以參考一下安裝過程。

## 安裝 XAMPP

建議優先安裝 `Windows x64 v8.1.17 版本`

<https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/8.1.17/xampp-windows-x64-8.1.17-0-VS16-installer.exe/download>

筆者這邊省略安裝過程。

## 安裝 Oracle Instant Client 驅動程式

筆者公司是使用 `Oracle 11g`。

前輩使用的 Oracle Client 的版本為 `12.2.0.1.0`，那我就版本一樣沒有改。

驅動網址：<https://www.oracle.com/tw/database/technologies/instant-client/winx64-64-downloads.html>

### 解壓縮並移動全部 dll 檔案

首先我們下載完 Oracle Client，就直接解壓縮。

然後排序`檔案類型`，我們要的是 `應用程式擴充`，為 .dll 副檔名的檔案。

如下圖，我們全部複製。

![全部的 dll 檔案](/images/20230821_xampp-x64-oracle_instant-client/01.dll-files.png)

### 複製到 xampp\apache\bin 資料夾

![將 dll 移至 apache/bin 資料夾](/images/20230821_xampp-x64-oracle_instant-client/02.apache.png)

> 關鍵之一，如果今天我們使用 XAMPP 啟用 PHP 時，這邊沒有 dll 檔案時，我們的 OCI8 就沒辦法啟動。

### 複製到 xampp\php 資料夾

![將 dll 移至 xampp/php 資料夾](/images/20230821_xampp-x64-oracle_instant-client/03.php.png)

> 關鍵之二，如果今天我們 PHP 時，這邊沒有 dll 檔案時，使用 `php -m` 指令會顯示錯誤。

## 安裝 Php OCI8 插件

oci8 插件的說明：<https://pecl.php.net/package/oci8>

筆者目前在 `Windows` 最新版為 `3.2.1`。

而網頁中的描述也有提到 `Use 'pecl install oci8-3.2.1' to install for PHP 8.1.`，所以我們的 XAMPP 的 PHP 指定版本為 `8.1.17`。

> 關鍵之三，所以插件的版本與 PHP 的版本是互相關聯的。 `記得要安裝 ts 版本。`，你可以參考下圖。

![確認 PHP 有無支援 Thread Safety](/images/20230821_xampp-x64-oracle_instant-client/04.php_info.png)

### 移動 OCI8 插件的 dll 檔案

## 設定 php.ini

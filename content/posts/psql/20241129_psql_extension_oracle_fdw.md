---
title: "PSQL - Oracle FDW  - 連接 Oracle 資料庫前的準備(大坑)"
description: "使用 Oracle FDW 連接 Oracle 資料庫前的準備, 結果發現沒那麼單純 :)"
date: 2024-11-29T05:11:52Z
slug: "psql-extension-oracle-fdw"
categories:
  - Experience
tags:
  - Database
  - PostgreSQL
  - Oracle
hidden: false
comments: true
draft: false
---

# 前言

這是在研究 Oracle FDW 的時候發現的問題。

相關的 repository 可以參考 [https://github.com/laurenz/oracle_fdw](https://github.com/laurenz/oracle_fdw)

但因為 pg16 以前並沒有直接提供 dll 檔, 因為編譯問題導致一直無法把 PostgreSQL 直接透過 DBLINK 的方式連接 Oracle 資料庫。

# 環境說明

- Windows 10
- PostgreSQL 16
- Oracle Instant Client 19.25
- Oracle Database 19c

# 安裝步驟

## 安裝 Oracle Instant Client 全部檔案 (我是安裝 x64 版本, 19.25)

## 安裝 PostgreSQL (我是安裝 x64 版本, 16)

## 安裝 Visual Studio 2022 中的 msbuild 套件

## 編譯 oracle_fdw.dll

## 把 oracle_fdw.dll 複製到 PostgreSQL 的資料夾中

## 將 oracle_fdw.dll 設定為 PostgreSQL 的擴充程式

## 測試是否成功

我在正式環境已經成功，然後系統是 Windows Server 版。

# 參考文件

[CSDN - Windows系统oracle_fdw安装与查询sdo_geometry数据过程记录](https://blog.csdn.net/Ec1ips6/article/details/141605806)
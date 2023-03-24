---
title: "網頁原生表單 01 - 如何將表單更改為 Javascript 的函式送出 ?"
description: "如果不更改，按下 Enter 讓表單送出後會在網址列 URL 加上 ? (問號)."
date: 2023-03-24T08:24:11Z
slug: "form-submit-prevent"
categories:
    - Experience
tags:
    - HTML
math: 
license: 
hidden: false
comments: true
draft: true
---

# 前言

在網頁開發中，表單是最常見的元素之一。不管是在登入視窗、新增資料，都需要表單的元素進行開發。

但是當使用者提交表單時，預設情況下，瀏覽器會將表單數據轉換為 URL 字符串，並在網址末尾添加問號和表單數據。

例如說我表單中有一個 `name` 的欄位，填寫了 `John`。這時候送出表單會發送什麼事 ?

```bash
# 在網址後面加上 ?name=John
http://localhost/?name=John
```

然而，這種情況可能會導致安全性問題或頁面顯示不佳。

> 筆者的情況就是出現 `?` 導致跳轉至首頁失敗

重點：

在這篇文章中，我們將介紹如何使用 JavaScript 預設提交表單，避免 URL 中顯示問號和表單數據。

# 解決方式

```html
<template>
  <v-app id="inspire">
    <!-- Vue2 - 使用套件 Vuetify 表單 -->
    <v-form ref="form" lazy-validation @submit.prevent="login">
      <!-- 帳號欄位 -->
      <v-text-field 
        v-model="form_data.name" 
        :rules="rules.name" 
        label="帳號"
        required
      ></v-text-field>
      <!-- 密碼欄位 -->
      <v-text-field 
      v-model="form_data.password" 
      :append-icon="show_pwd ? 'mdi-eye' : 'mdi-eye-off'" 
      :type="show_pwd ? 'text' : 'password'" 
      label="密碼" 
      :rules="rules.password" 
      @click:append="show_pwd = !show_pwd"
      required
      ></v-text-field>
      <!-- 送出按鈕 -->
      <v-btn dark color="primary" block class="mt-8" type="submit">登入</v-btn>
    </v-form>
  </v-app>
</template>

<script>
export default {
  name: "LoginPage",
  data: () => ({ ... }), // 非探討區域
  methods: {
    login() {
      this.$refs.form.validate(); // 驗證
      if (this.account && this.pwd) { 
        this.$router.push("/"); // 跳轉頁面
      } else {
        console.log("login failed"); // 顯示錯誤
      }
    }
  }
};
</script>
```

眼尖的你應該有發現我的 `login()` 如何觸發 ?

在 form 元素使用 `@submit.prevent` 來觸發 submit 事件 !

其實這個問題沒有太多技巧，就想做這個紀錄，讓自己知道其實 `form` 元素還有其他事情可以做。

# 後續

除了 submit.prevent 以外，form 元素中還有以下的事件修飾符：

.lazy：在表單提交時只驗證那些已經被修改過的表單欄位，而不是驗證所有欄位。這樣可以提高表單提交的效率。

.number：將表單欄位的值轉換為數字，如果轉換失敗則返回空字符串。

.trim：自動去除表單欄位值的開頭和結尾的空格。

.lazy + .number + .trim：同時應用上面的三種事件修飾符，即只驗證修改過的欄位、轉換為數字並去除空格。

除了這些事件修飾符之外，還可以使用 .stop、.capture、.self、.once 等事件修飾符。.stop 可以停止事件的傳播，.capture 可以在元素自身之前處理事件，.self 可以限制事件只在元素本身觸發，.once 可以只觸發一次事件。

> 這些都是未來可以研究的東西，那麼我先將資訊貼在這 !
>
> 希望之後我能再加強這部分的事件進行了解。
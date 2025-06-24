---
title: "Ubuntu 磁碟空間升級"
description: "Ubuntu Server 磁碟空間升級"
date: 2025-06-23T00:02:09+08:00
slug: "ubuntu-expand-space"
categories:
    - Linux
tags:
    - Ubuntu
math: false
license: CC BY-NC-SA 4.0
hidden: false
comments: true
draft: false
---

# 前言

```bash
ubuntu@dev-server:~/dev/cms$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              790M  1.4M  789M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   48G   32G   14G  70% /
tmpfs                              3.9G     0  3.9G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          2.0G  188M  1.7G  11% /boot
tmpfs                              790M   12K  790M   1% /run/user/1000
```

發現 `/dev/mapper/ubuntu--vg-ubuntu--lv` 空間是只有 48G

VMware 的磁碟空間已經確定提升到 100G，但是都還需要進行手動操作。

然後每次問 GPT 磁碟空間升級的指令，結果都不太相同，

這次紀錄一下升級最快的方式。

# 如何提升空間

先透過 `lsblk` 看看磁碟空間的使用情況

```bash
ubuntu@dev-server:~/dev/cms$ lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0  100G  0 disk 
├─sda1                      8:1    0    1M  0 part 
├─sda2                      8:2    0    2G  0 part /boot
└─sda3                      8:3    0   98G  0 part 
  └─ubuntu--vg-ubuntu--lv 252:0    0   49G  0 lvm  /
sr0                        11:0    1  2.6G  0 rom
```

可以看到 `/dev/mapper/ubuntu--vg-ubuntu--lv` 空間是只有 49G

但是 sda3 空間是 98G，表示磁碟空間尚未使用 (跟 `df` 的結果不同)

# 升級空間

```bash
sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
```

## 範例

```bash
ubuntu@dev-server:~/dev/cms$ sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
  Size of logical volume ubuntu-vg/ubuntu-lv changed from <49.00 GiB (12543 extents) to <98.00 GiB (25087 extents).
  Logical volume ubuntu-vg/ubuntu-lv successfully resized.
```



# 擴展文件系統

```bash
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```

## 範例

```bash
ubuntu@dev-server:~/dev/cms$ sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
resize2fs 1.47.0 (5-Feb-2023)
Filesystem at /dev/mapper/ubuntu--vg-ubuntu--lv is mounted on /; on-line resizing required
old_desc_blocks = 7, new_desc_blocks = 13
The filesystem on /dev/mapper/ubuntu--vg-ubuntu--lv is now 25689088 (4k) blocks long.
```

# 檢查文件系統

```bash
df -h
```

## 範例

```bash
ubuntu@dev-server:~/dev/cms$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              790M  1.4M  789M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   97G   32G   61G  35% /
tmpfs                              3.9G     0  3.9G   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          2.0G  188M  1.7G  11% /boot
tmpfs                              790M   12K  790M   1% /run/user/1000
```

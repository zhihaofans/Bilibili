# Bilibili小黑屋


### 数据来源
[Bilibili官方](http://www.bilibili.com/blackroom/)

### 官方API
(由我本人抓包得到，非官方公布的)

地址
`http://www.bilibili.com/blackroom/web/blocked_info?originType=0&pageNo=1&pageSize=20`

### 介绍

Bilibili小黑屋爬虫及数据备份

### 已知BUG

~~请在 `Bilibili/blackroom/python` 路径下执行 [`Bilibili/blackroom/python/start.py`](python/start.py) ,否则将导致数据保存路径错误~~(已修复)

### 数据

- [上次更新时间](update.txt) (UNIX时间戳，秒)
- [最新数据](data/blackroom.json)
- [永久封禁列表](data/forever/)
- [限时封禁用户历史列表](data/user/) (暂时不考虑删除,以后可能会考虑删除)
- [所有封禁历史列表](data/user/) (暂时不考虑删除,以后可能会考虑删除)
- [每次抓包数据备份](data/backup/) 

### 基于
语言: 

- `Python 3.6.1`  (Windows)

模块: 
- `requests` ([下载地址](http://cn.python-requests.org/zh_CN/latest/user/install.html))


### 注意

-  [auto-push.py](python/auto-push.py) 未完成

### 其他
本脚本仅作学习使用，由该脚本生成的数据仅作学习参考使用。
本项目随时可能因为某些原因原因删除。

### LICENSE
- [Apache-2.0](LICENSE)

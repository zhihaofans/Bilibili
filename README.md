# Bilibili-BlackList
Bilibili小黑屋爬虫及数据备份

数据来源
-
[Bilibili官方](http://www.bilibili.com/blackroom/)

官方API
-
(由我本人抓包得到，非官方公布的)

### 地址：
`http://www.bilibili.com/blackroom/web/blocked_info?originType=0&pageNo=1&pageSize=20`

### 介绍:

待完善

数据
-

- [小黑屋列表](blackroom/data/blackListsData.json)
- [曾被封禁用户列表](blackroom/data/blackListsUserData.json)

爬虫基于
-
- 语言: `Python 3.5.2`

- 模块: `requests` ([下载地址](http://cn.python-requests.org/zh_CN/latest/user/install.html))

LICENSE
-
- [Apache-2.0](LICENSE)
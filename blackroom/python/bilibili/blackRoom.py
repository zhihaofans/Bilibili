#!/usr/bin/python3
# -*-coding:utf-8 -*-
# ProjectName:Bilibili小黑屋 模块
# Author:zhihaofans
# PythonVersion:3.x
import requests
"""
Bilibili小黑屋 模块

调用 requests 模块，使用前请安装

"""


def getData(page=None, pageSize=20, originType=0):
    # 如果page=0则一直获取直到空白
    print("page:", page)
    if page == None:
        listData = []
        goOnGet = True
        nowPage = 1
        while goOnGet:
            print("page:", nowPage)
            a = "https://www.bilibili.com/blackroom/web/blocked_info?originType="\
                + str(originType) + "&pageSize=" + \
                str(pageSize) + "&pageNo=" + str(nowPage)
            b = requests.get(a).json()
            if b["code"] == 0:
                if len(b["data"]) > 0:
                    listData=listData + b["data"]
                else:
                    print("\n", "page:", nowPage,  "empty", "\n")
                    goOnGet = False

            else:
                print("\n", "page:", nowPage, "\n",
                      b["msg"], "(", b["code"], ")", "\n")
                goOnGet = False
            nowPage = nowPage + 1
        return listData
    else:
        a = "https://www.bilibili.com/blackroom/web/blocked_info?originType="\
            + str(originType) + "&pageSize=" + \
            str(pageSize) + "&pageNo=" + str(page)
        b = requests.get(a).json()
        if b["code"] == 0:
            if len(b["data"]) == 0:
                print("\n", "page:", page,  "empty", "\n")
            return b["data"]

        else:
            print("\n", "page:", page, "\n",
                  b["msg"], "(", b["code"], ")", "\n")
            return None


def getAllUser(data):
    """
    input something form getData()

    return all users's uid

    [
        1,

        2,

        3
    ]

    if blockedForever=True then blockedDays=0
    """
    userList = []
    nu = 0
    while nu < len(data):
        userList.append(data[nu]["uid"])
        nu + 1
    return userList


def getForeverList(data):
    """
    input something form getData()
    """
    users = []
    nu = 0
    while nu < len(data):
        if data[nu]['blockedForever']:
            users.append(data[nu])
        nu = nu + 1
    return users


def getNoForeverList(data):
    """
    input something form getData()
    """
    users = []
    nu = 0
    while nu < len(data):
        user = data[nu]
        if user['blockedForever'] == False:
            users.append(user)
        nu = nu + 1
    return users

#!/usr/bin/python3
# -*-coding:utf-8 -*-
# ProjectName:Bilibili小黑屋爬虫v2
# Author:zhihaofans
# Github:https://github.com/zhihaofans/Bilibili/tree/master/blackroom
# PythonVersion:3.x
import requests
import os
import json
import time
import platform
from bilibili import blackRoom
from zhihaofans import file as f

savePath = f.getUpPath(os.path.split(os.path.realpath(__file__))[0]) + '/data/'
savePath_forever = savePath + '/forever/'
savePath_noForever = savePath + '/user/'
savePath_backup = savePath + '/backup/'
savePath_history = savePath + '/history/'

blList = []

if platform.system() == "Windows":
    savePath = savePath.replace('/', '\\')
    savePath_forever = savePath_forever.replace('/', '\\')
    savePath_noForever = savePath_noForever.replace('/', '\\')
    savePath_backup = savePath_backup.replace('/', '\\')
    savePath_history = savePath_history.replace('/', '\\')


def saveData(data):
    thisTime = str(time.time()).split(".")[0]
    f.write(savePath + "blackroom.json", json.dumps(data))
    # 备份数据
    print("备份数据")
    f.write(savePath_backup + thisTime + ".json", json.dumps(data))
    # 历史数据
    print("历史数据")
    for a in data:
        f.write(savePath_history + str(a['id']) + ".json", json.dumps(a), True)
    # 永久封禁
    print("永久封禁与限时封禁数据分开按用户储存")
    for b in data:
        if b["blockedForever"]:
            f.write(savePath_forever +
                    str(b['uid']) + ".json", json.dumps(b), True)
        else:
            filePath = savePath_noForever + str(b['uid']) + "/"
            f.mk(filePath)
            f.write(filePath + str(b['id']) + ".json", json.dumps(b), True)
    f.write(savePath + "update.txt", thisTime)
    print(thisTime)


def mkdirs():
    f.mk(savePath_forever)
    f.mk(savePath_noForever)
    f.mk(savePath_backup)
    f.mk(savePath_history)


def main():
    print(savePath)
    input('This path,OK?')
    mkdirs()
    print("开始抓取小黑屋数据")
    brList = blackRoom.getData()
    print("保存数据")
    saveData(brList)
    print("抓取完成")
    input("按回车退出")
    exit()


if __name__ == '__main__':
    main()

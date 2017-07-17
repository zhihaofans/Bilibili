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
from bilibili import blackRoom
from zhihaofans import file as f

savePath = f.getUpPath(f.getMyPyPath()) + '/data/'
savePath_forever = savePath + '/forever/'
savePath_noForever = savePath + '/user/'
savePath_backup = savePath + '/backup/'
savePath_history = savePath + '/history/'

blList = []
updateTime = 0
gitPath = 'git'
gitLocalBranch = 'origin'
gitRemoteBranch = 'master'


def saveData(data):
    thisTime = str(time.time()).split(".")[0]
    updateTime = thisTime
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


def mkdirs():
    f.mk(savePath_forever)
    f.mk(savePath_noForever)
    f.mk(savePath_backup)
    f.mk(savePath_history)


def getPush():
    cmdPath = os.getcwd()
    os.chdir(f.getUpPath(f.getMyPyPath()))
    print(getCmd("git add *"))
    print(getCmd("git status"))
    print(getCmd("git commit -m \"Auto update blackroom(" + str(updateTime) + "\")"))
    print(getCmd("git push " + gitLocalBranch + " " + gitRemoteBranch))


def getCmd(cmdText):
    return os.popen(cmdText).read()


def main():
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

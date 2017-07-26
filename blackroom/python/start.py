#!/usr/bin/python3
# -*-coding:utf-8 -*-
# ProjectName:Bilibili小黑屋爬虫v2
# Author:zhihaofans
# Github:https://github.com/zhihaofans/Bilibili/tree/master/blackroom
# PythonVersion:3.x
import os
import json
import time
import platform
import requests


def fWrite(filePath, fileData, stopIfExisted=False):
    if stopIfExisted and os.path.exists(filePath):
        return None
    with open(filePath, "w") as ff:
        return ff.write(fileData)


def fGetUpPath(path):
    inputPath = path
    if inputPath[-1] == '/' or inputPath[-1] == '\\':
        inputPath = inputPath[:-1]
    return os.path.split(inputPath)[0]


def fMk(path, mode=0o777):
    try:
        os.makedirs(name=path, mode=mode, exist_ok=True)
        return True
    except:
        return False

savePath = fGetUpPath(os.path.split(os.path.realpath(__file__))[0]) + '/data/'
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
    fWrite(savePath + "blackroom.json", json.dumps(data))
    # 备份数据
    print("备份数据")
    fWrite(savePath_backup + thisTime + ".json", json.dumps(data))
    # 历史数据
    print("历史数据")
    for a in data:
        fWrite(savePath_history + str(a['id']) + ".json", json.dumps(a), True)
    # 永久封禁
    print("永久封禁与限时封禁数据分开按用户储存")
    for b in data:
        if b["blockedForever"]:
            fWrite(savePath_forever +
                   str(b['uid']) + ".json", json.dumps(b), True)
        else:
            filePath = savePath_noForever + str(b['uid']) + "/"
            fMk(filePath)
            fWrite(filePath + str(b['id']) + ".json", json.dumps(b), True)
    fWrite(savePath + "update.txt", thisTime)
    print(thisTime)

def getData(originType=0):
    a = "https://www.bilibili.com/blackroom/web/blocked_info?originType="\
        + str(originType) + "&pageSize=0"
    b = requests.get(a).json()
    if b["code"] == 0:
        return b["data"]
    else:
        print(b["msg"], "(", b["code"], ")", "\n")
        return False


def main():
    print(savePath)
    input('This path,OK?')
    fMk(savePath_forever)
    fMk(savePath_noForever)
    fMk(savePath_backup)
    fMk(savePath_history)
    print("开始抓取小黑屋数据")
    brList = getData()
    if brList is False:
        print("获取失败,END")
        input("按回车退出")
        exit()
    print("保存数据")
    saveData(brList)
    print("抓取完成")
    input("按回车退出")
    exit()


if __name__ == '__main__':
    main()

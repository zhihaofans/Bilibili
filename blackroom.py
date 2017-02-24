#!/usr/bin/python3
# -*-coding:utf-8 -*-
# ProjectName:Bilibili小黑屋爬虫
# Author:zhihaofans
# Github:https://github.com/zhihaofans/Bilibili-BlackList
# PythonVersion:3.x
import requests
import os
import json
import time
setting_savePath='blackroom/data/'
#http://www.bilibili.com/blackroom/web/blocked_info?originType=0&pageNo=3&pageSize=20
def function():
    pass
def getBlackList(_page):
    listUrl='http://www.bilibili.com/blackroom/web/blocked_info?originType=0&pageSize=20&pageNo='+_page
    return requests.get(listUrl).json()
def getBlackLists():
    getFinish=False
    getPage=1
    blackListsData=[]
    blackListsUserData=[]
    while getFinish==False:
        print("第",getPage,"页")
        blackListData={}
        blackListData=getBlackList(str(getPage))
        blackListNum=len(blackListData['data'])
        if blackListNum==0:
            print("这一页没有东西\n共抓取了",getPage-1,"页(",len(blackListsData),"个数据)")
            getFinish=True
        elif blackListData['code']!=0:
            print("返回数据错误\n",json.dumps(blackListData))
            getFinish=True
        else:
            blackListNowNum=0
            while blackListNowNum<blackListNum:
                blackListNow={}
                blackListNow=blackListData['data'][blackListNowNum]
                blackListsData.append(blackListNow)
                blackListsUserData.append(blackListNow['uid'])
                if blackListNow['blockedForever']:
                    blockDay="永久封禁"
                else:
                    blockDay=str(blackListNow['blockedDays'])+"天"
                print("用户id:",blackListNow['uid'],"\n用户名称:",blackListNow['uname'],"\n原因:",blackListNow['punishTitle'],"封禁时间:",blockDay,"\n\n")
                blackListNowNum=blackListNowNum+1
            getPage=getPage+1
            print("\n\n等待一秒\n\n\n")
            time.sleep(1)
    saveTxt(setting_savePath+"blackListsData.json",json.dumps(blackListsData))
    saveTxt(setting_savePath+"blackListsUserData.json",json.dumps(blackListsUserData))
def saveTxt(_filepath,txtData):
    if os.path.exists(os.path.dirname(_filepath)):
        print("saveTxt:目录已存在")
    else:
        os.makedirs(os.path.dirname(_filepath))
    if os.path.exists(_filepath):
        os.remove(_filepath)
    fo = open(_filepath, "w",encoding='utf-8')
    print ("文件名: ", fo.name)
    fo.write(txtData)
    fo.close()
def main():
    print("开始抓取小黑屋数据")
    getBlackLists()
    print("抓取完成")
    input("按回车退出")
    exit()
if __name__=='__main__':  
    main()
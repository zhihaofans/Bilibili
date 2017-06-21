#!/usr/bin/python3
# -*-coding:utf-8 -*-
# ProjectName:Zhihaofans的网络模块
# Author:zhihaofans
# PythonVersion:3.x
"""
requests模块的快捷调用

-----

请自行安装requests

代理demo

proxy = {

    "http": "http://10.10.1.10:3128",

    "https": "http://10.10.1.10:1080",

    'http': 'socks5://user:pass@host:port',

    'https': 'socks5://user:pass@host:port'

    }

socks代理需要另外安装pip install requests[socks]
"""
import requests


def g(url, header=None, cookies=None, proxy=None):
    return requests.get(url, header=header, proxies=proxy)


def p(url, postData=None, header=None, cookies=None, proxy=None):
    """
    postData = {'key1': 'value1', 'key2': 'value2'}

    """
    return requests.post(url, data=postData, header=header, proxies=proxy)

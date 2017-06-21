#!/usr/bin/python3
# -*-coding:utf-8 -*-
# ProjectName:Zhihaofans的文件模块
# Author:zhihaofans
# PythonVersion:3.x
import os
import shutil


def read(filePath):
    with open(filePath) as f:
        return f.read()


def write(filePath, fileData,stopIfExisted=False):
    if stopIfExisted and exists(filePath):
        return None
    with open(filePath, "w") as f:
        return f.write(fileData)


def cp(old, new, force=False):
    if os.path.exists(old):
        if os.path.exists(old):
            if force:
                if os.path.isfile:
                    try:
                        shutil.copyfile(old, new)
                        return True
                    except:
                        return False
                else:
                    try:
                        shutil.copytree(old, new, True)
                        return True
                    except:
                        return False
            else:
                return False
        else:
            if os.path.isfile:
                try:
                    shutil.copyfile(old, new)
                    return True
                except:
                    return False
            else:
                try:
                    shutil.copytree(old, new, True)
                    return True
                except:
                    return False
    else:
        return False


def mv(old, new, force=False):
    if os.path.exists(old):
        if force:
            if os.path.isfile(new):
                try:
                    os.remove(new)
                except:
                    return False
            else:
                try:
                    shutil.rmtree(new)
                except:
                    return False
            try:
                shutil.move(old, new)
                return True
            except:
                return False
    else:
        try:
            shutil.move(old, new)
            return True
        except:
            return False


def mk(path, mode=0o777):
    try:
        os.makedirs(name=path, mode=mode, exist_ok=True)
        return True
    except:
        return False


def rm(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            try:
                os.removedirs(path)
                return True
            except:
                return False
        else:
            try:
                os.remove(path)
                return True
            except:
                return False
    else:
        return False


def exists(path):
    return os.path.exists(path)


def isdir(path):
    return os.path.isdir(path)
def getDir(path):
    return os.path.dirname(path)
def getFilename(path):
    return os.path.basename(path)
def getExtname(path):
    return os.path.splitext(path)[1]
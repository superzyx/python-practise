#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date: 2019/08/09
# usage:check dirctory,files


import os

dirC = 0
filC = 0
def getCount(path):
    for files in os.listdir(path):
        filepath = os.path.join(path, files)
        if os.path.isdir(filepath):
            global dirC
            dirC += 1
            getCount(filepath)
        else:
            global filC
            filC += 1
    return dirC, filC
a,b = getCount('D:\PycharmProjects\python-practise\day05_python_adavnced')
print('dirCount: {}, fileCount: {}'.format(dirC, filC))
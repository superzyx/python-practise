#!/usr/bin/env python3
# ^3^ coding=utf-8
#
# author: superzyx
# date: 2019/09/08
# usage: the forth one of exams


# 4.请使用Python代码对[23, 14, 12, 21, 45, 99, 34, 42]排序， 请使用冒泡排序

list01 = [23, 14, 12, 21, 45, 99, 34, 42]

for i in range(len(list01)):
    for j in range(len(list01) - i - 1):
        if list01[j] > list01[j+1]:
            list01[j], list01[j+1] = list01[j+1], list01[j]
print(list01)
#!/usr/bin/env python3
# ^3^ coding=utf-8
#
# author: superzyx
# date: 2019/09/08
# usage: the seventeenth one of exams


# 17.利用闭包来实现一个可以从任意初始值开始计数的计步器

def counters(init):
    def count(total):
        total = init + 1
        print(total)
    return count

d = counters(3)
d(3)
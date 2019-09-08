#!/usr/bin/env python3
# ^3^ coding=utf-8
#
# author: superzyx
# date: 2019/09/08
# usage: the second one of exams


# 2.请使用python代码反转句子'long with me play game'  ->> 'game play me with long'
str01 = 'long with me play game'
list01 =  str01.split()
list01.reverse()
str02 = list01[0] + ' ' + list01[1] + ' ' + list01[2] + ' ' + list01[3] + ' ' + list01[4]
print(str02)
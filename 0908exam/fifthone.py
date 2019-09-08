#!/usr/bin/env python3
# ^3^ coding=utf-8
#
# author: superzyx
# date: 2019/09/08
# usage: the second one of exams


# 5.请使用Python代码对{'tom': 198, 'jerry': 34, 'hale': 400, 'tony': 23}进行排序，请使用高阶函数

dict01 = {'tom': 198, 'jerry': 34, 'hale': 400, 'tony': 23}

dict01 = dict(sorted(dict01.items(), key=lambda x:x[1], reverse=True))
print(dict01)
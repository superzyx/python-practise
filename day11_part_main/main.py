#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/19
# usage: main function


# from source_func.packdge import log_Analysis
#
# inr = input('input:')
# if hasattr(log_Analysis, inr):
#     ly = getattr(log_Analysis, inr)
#     ly()

url = input('输入：')
inf = __import__('{}.{}.{}'.format(url.split('/')[-4], url.split('/')[-3], url.split('/')[-2]), fromlist=True)
if hasattr(inf , url.split('/')[-1]):
    ins = getattr(inf,url.split('/')[-1])
    ins()
else:
    print('404')


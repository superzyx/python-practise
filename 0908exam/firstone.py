#!/usr/bin/env python3
# ^3^ coding=utf-8
#
# author: superzyx
# date: 2019/09/08
# usage: the first one of exams


# 1.请使用Python代码分析日志(access_log)中 IP排名//状态码分布//最热资源排名(请写出各部分具体代码)
ip_dict = {}
state_dict = {}
hot_dict = {}
state_tuple = ('200', '300', '400', '404', '499', '500', '505')
with open(file='./source/access_log', mode='r', encoding='utf-8')as file:
    for con in file:
        ip_dict.setdefault(con.split()[0], 0)
        ip_dict[con.split()[0]] += 1
        if con.split()[8] in state_tuple:
            state_dict.setdefault(con.split()[8], 0)
            state_dict[con.split()[8]] += 1
        hot_dict.setdefault(con.split()[6], 0)
        hot_dict[con.split()[6]] += 1


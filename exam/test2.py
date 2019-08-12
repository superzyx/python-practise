#!/usr/bin/env python3
# coding=utf8
#
# author:superzyx
# date:2019/08/09
# usage:exam


import json
dict_scode ={}
with open(file='../day03_python_dict,set/reading/access_log', mode='r', encoding='utf8')as file01:
    for con in file01.readlines():
        if con.split()[8] in dict_scode.keys():
            dict_scode[con.split()[8]] += 1
        else:
            dict_scode[con.split()[8]] = 1
print(dict_scode)


with open(file='./scode.json', mode='w', encoding='utf8')as file02:
    file02.write(json.dumps(dict_scode))
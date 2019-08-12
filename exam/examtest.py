#!/usr/bin/env python3
# coding=utf8
#
# author:superzyx
# date:2019/08/09
# usage:exam


import json
dict_pv ={}
with open(file='../day03_python_dict,set/reading/access_log', mode='r', encoding='utf8')as file01:
    for con in file01.readlines():
        if con.split()[0] in dict_pv.keys():
            dict_pv[con.split()[0]] += 1
        else:
            dict_pv[con.split()[0]] = 1
print(dict_pv)
dict_pv = sorted(dict_pv.items(), key=lambda x:x[1], reverse=True)
dict_pv = dict(dict_pv[:10])
print(dict_pv)
with open(file='./pv.json', mode='w', encoding='utf8')as file02:
    file02.write(json.dumps(dict_pv))
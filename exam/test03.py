#!/usr/bin/env python3
# coding=utf8
#
# author:superzyx
# date:2019/08/09
# usage:exam


import json
dict_ipp ={}
with open(file='../day03_python_dict,set/reading/access_log', mode='r', encoding='utf8')as file01:
    for con in file01.readlines():
        if con.split()[6] in dict_ipp.keys():
            dict_ipp[con.split()[6]] += 1
        else:
            dict_ipp[con.split()[6]] = 1
print(dict_ipp)
dict_ipp = sorted(dict_ipp.items(), key=lambda x:x[1], reverse=True)
dict_ipp = dict(dict_ipp[:10])
print(dict_ipp)
with open(file='./ipaddr.json', mode='w', encoding='utf8')as file02:
    file02.write(json.dumps(dict_ipp))
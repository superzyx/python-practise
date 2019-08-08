#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/08
# usage: function


import json


def analysis(path):
    """
    analysis log
    :param path: the path of files
    :return: 访问量，状态码，最热资源
    """
    with open(file=path, mode='r', encoding='utf8')as file01:
        dict_ip = {}
        dict_status = {}
        dict_resource = {}
        for content in file01.readlines():
            if content.split()[0] in dict_ip.keys():
                dict_ip[content.split()[0]] += 1
            elif content.split()[0] not in dict_ip.keys():
                dict_ip[content.split()[0]] = 1
            if content.split()[8] in dict_status.keys():
                dict_status[content.split()[8]] += 1
            elif content.split()[8] not in dict_status.keys():
                dict_status[content.split()[8]] = 1
            if content.split()[6] in dict_resource.keys():
                dict_resource[content.split()[6]] += 1
            elif content.split()[6] not in dict_resource.keys():
                dict_resource[content.split()[6]] = 1
    return dict_ip, dict_status, dict_resource

def top(path, dict_ip, dict_status, dict_resource):
    """
    排列数据，选出前十名
    :param dict_ip: ip访问量字典
    :param dict_status: 状态码字典
    :param dict_resource: 最热资源字典
    :return: json格式文件
    """
    dict_ip = dict(sorted(dict_ip.items(), key=lambda x:x[1], reverse=False)[:10])
    dict_status = dict(sorted(dict_status.items(), key=lambda x:x[1], reverse=False)[:10])
    dict_resource = dict(sorted(dict_resource.items(), key=lambda x:x[1], reverse=False)[:10])
    print(dict_ip)
    with open(file=path, mode='w', encoding='utf8')as file02:
        a1 = json.dumps(dict_ip, ensure_ascii=False)
        a2 = json.dumps(dict_status, ensure_ascii=False)
        a3 = json.dumps(dict_resource, ensure_ascii=False)
        file02.write(a1)
        file02.write('\n')
        file02.write(a2)
        file02.write('\n')
        file02.write(a3)
        file02.write('\n')
    return a1,a2,a3

dict01, dict02, dict03 = analysis('../day03_python_dict,set/reading/access_log')
print(dict01,'\n', dict02,'\n', dict03)
str01, str02, str03 = top('../day03_python_dict,set/reading/all_log', dict01, dict02, dict03)
print(str01, '\n', str02, '\n', str03)



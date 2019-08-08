#!/usr/bin/env bash
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/08
# usage:理解闭包,分析log


def analysis(path):
    """
    select the pva nd  uv
    :param path: the path of file
    :return: dict
    """
    def check_analysis(dict01):
        if len(dict01) != 0 or type(dict01) != dict:
            return 'gun'
        with open(file=path, mode='r', encoding='utf8')as file01:
            for con in file01.readlines():
                if con.split()[0] in dict01.keys():
                    dict01[con.split()[0]] += 1
                else:
                    dict01[con.split()[0]] = 1
        return dict01
    return check_analysis

diy = analysis('../day03_python_dict,set/reading/access_log')
dict02 = diy({})
print(dict02)

list01 = [element for element in dict02.items()]
list01 = sorted(list01, key=lambda x:x[1], reverse=False)
print(list01[-10:])

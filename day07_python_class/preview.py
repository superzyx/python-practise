#!/usr/bin/env python3
# ^3^ coding= utf8
#
# author: superzyx
# date: 2019/08/13
# usage: preview oop


class Website():
    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def createMethod(cls,filename):
        return cls(filename)

    def count_ip(self):
        list01 = []
        with open(file= self.filename, mode='r', encoding='utf8')as file01:
            for item in file01.readlines():
                list01.append(item.split()[0])
        return len(list01), len(set(list01))

    def con_status(self):
        dict01 = {}
        with open(file= self.filename, mode='r', encoding='utf8')as file02:
            for item in file02.readlines():
                if item.split()[8] in dict01.keys():
                    dict01[item.split()[8]] += 1
                else:
                    dict01[item.split()[8]] = 1
        return dict01

    def hot_rescource(self):
        dict02 = {}
        with open(file= self.filename, mode='r', encoding='utf8')as file03:
            for item in file03.readlines():
                if item.split()[6] in dict02.keys():
                    dict02[item.split()[6]] += 1
                else:
                    dict02[item.split()[6]] = 1
        return dict02

param = Website.createMethod('../day03_python_dict,set/reading/access_log')
a, b = param.count_ip()
c = param.con_status()
d = param.hot_rescource()
print('''
    pv = {}
    uv = {}
    status = {}
    hot = {}
    
    '''.format(a,b,c,d))
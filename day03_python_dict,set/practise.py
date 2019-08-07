#!/usr/bin/env bash
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/07
# usage: python practise


import json


dict01 = {}
numcao = 0
numliu = 0
numzhu =0
numsun =0
with open(file='./reading/kingdoms.txt', mode='r+', encoding='utf8') as file01:
    content = file01.readlines()
    for element in content:
        for skr in range(len(element)):
            if element[skr] == '曹'  and element[skr+1] == '操' :
                numcao += 1
                dict01.update([('曹操', numcao)])
            if element[skr] == '刘'  and element[skr+1] == '备' :
                numliu += 1
                dict01.update([('刘备', numliu)])
            if element[skr] == '卧'  and element[skr+1] == '龙' :
                numzhu += 1
                dict01.update([('卧龙', numzhu)])
            if element[skr] == '孙'  and element[skr+1] == '权' :
                numsun += 1
                dict01.update([('孙权', numsun)])
print(dict01)

dict_bing = {}.fromkeys(['青龙偃月刀', '丈八蛇矛', '赤兔', '雌雄'])
num_qing = 0
num_zhang = 0
num_chi = 0
num_ci = 0
with open(file='./reading/kingdoms.txt', mode='r+', encoding='utf8') as file01:
    for sen in file01.readlines():
        if '青龙偃月刀' in sen:
            num_qing += 1
            dict_bing['青龙偃月刀'] = num_qing
        if '丈八蛇矛' in sen:
            num_zhang += 1
            dict_bing['丈八蛇矛'] = num_zhang
        if '赤兔' in sen:
            num_chi += 1
            dict_bing['赤兔'] = num_chi
        if '雌雄' in sen:
            num_ci += 1
            dict_bing['雌雄'] =num_ci
print(dict_bing)

list01 = []
for item in dict01.items():
    list01.append(item)
# print(list01)
for i in range(len(list01)):
    for j in range(len(list01) - i - 1):
        if list01[j][1] < list01[j+1][1]:
            list01[j], list01[j+1] = list01[j+1] , list01[j]
dict_man = dict(list01)
print(dict_man)

list02 = []
for item in dict_bing.items():
    list02.append(item)
for i in range(len(list02)):
    for j in range(len(list02) - i - 1):
        if list02[j][1] < list02[j+1][1]:
            list02[j], list02[j+1] = list02[j+1] , list02[j]
dict_bing = dict(list02)
print(dict_bing)

with open(file='./reading/dict.json', mode='w', encoding='utf8') as file01:
    file01.write(json.dumps(dict_man))
    file01.write(json.dumps(dict_bing))

dict_ping = {}
with open(file='./reading/access_log', mode='r+', encoding='utf8')as file02:
    file_content = '123'
    while file_content != None :
        file_content = file02.readline()
        # if file_content == {}:
        #     print('jjjj')
        list03 = file_content.split()
        if list03 ==[]:
            # print('jjjjjjj')
            break
        # print(list03[0])
        if list03[0] in dict_ping.keys():
            dict_ping[list03[0]] += 1
        else:
            dict_ping[list03[0]] = 1
    print(dict_ping)
list06 = []
for item in dict_ping.items():
    list06.append(item)
for i in range(10):
    for j in range(len(list06) - i -1 ):
        if list06[j][1] > list06[j+1][1]:
            list06[j], list06[j+1] = list06[j+1], list06[j]
list06 = list06[-10:]
print(list06)
dict_ping = dict(list06)


with open(file='./reading/access.json', mode='w', encoding='utf8')as file03:
    file03.write(json.dumps(dict_ping, ensure_ascii= False))

with open(file='./reading/access_log', mode='r+', encoding='utf8')as file04:
    file_content = '123'
    dict_stat ={}
    while file_content != None:
        file_content = file04.readline()
        list05 = file_content.split()
        if list05 == []:
            break
        # print(list05[8])
        if list05[8] in dict_stat.keys():
            dict_stat[list05[8]] += 1
        else:
            dict_stat[list05[8]] = 1
    print(dict_stat)

    with open(file='./reading/netstatus.json', mode='w', encoding='utf8')as file05:
        file05.write(json.dumps(dict_stat, ensure_ascii= False))

with open(file="./reading/access_log", mode='r+', encoding='utf8')as file06:
    dict_yum = {}
    file_content ='123'
    while file_content != None:
        file_content = file06.readline()
        list07 = file_content.split()
        if list07 == []:
            break
        # print(list07[6])
        if list07[0] in dict_yum.keys():
            len01 = len(list07[6].split('/'))
            dict_yum[list07[0]+list07[6]] = len01
        else:
            dict_yum[list07[0]] = len(list07[6].split('/'))
print(dict_yum)

list08 = []
for item in dict_yum.items():
    list08.append(item)
for i in range(10):
    for j in range(len(list08) - i -1):
        if list08[j][1] > list08[j+1][1]:
            list08[j], list08[j+1] = list08[j+1], list08[j]
list08 = list08[-10:]
dict_yum = dict(list08)
print(dict_yum)
# print('192.168'+ len)

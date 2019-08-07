#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/07
# usage:dict,set practise


ips = {"192.168.161.23" : 92 , "1.1.1.1" : 777 , "9.95.57.53" : 21}
# list01 = []
# for item in ips.items():
#     list01.append(item)
# print(list01)
# for index in range(len(list01)):
#     for j in range(len(list01) - index -1):
#         if list01[index][1] < list01[index+1][1]:
#             list01[index], list01[index+1] = list01[index+1], list01[index]
# print(list01)
# ips01 = dict(list01)
# print(ips01)

dict01 = {'afjaks;d' : 1 , 'name' : 'superzyx' , 'age' : '933'}
# print(dict01)
dict01.update([('work', 'progammer')])
print(dict01)
dict01['lived'] = 'yes'
print(dict01)
dict01.setdefault('sex')
dict01.setdefault('tele', '110')
print(dict01)

dict01.pop('age')
dict01.popitem()
print(dict01)

dict01['work'] = 'a good citizen'
print(dict01)
dict01.update([('lived', 'dead')])
print(dict01)

set01 = {1, 2, 3, 4, 5, 6}
set01.add(0)
print(set01)
set01.update([9,0,2])
print(set01)
set01.update("yesterday")
set01.remove(0)
print(set01)

print(list(set01))

dict02 = {}.fromkeys(['iname', 'type', 'name', 'size'])
print(dict02)

for keys in dict01.keys():
    print(keys)
for values in dict01.values():
    print(values)
for item in dict.items():
    print(item)
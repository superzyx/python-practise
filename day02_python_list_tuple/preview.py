#!/usr/bin/env python3
# ^3^coding=utf8
#
# author:superzyx
# date:2019/08/06
# usage:preview tuple,list,string


list01 = [1, 3, "jaishfas", True]
tuple01 = (1, 2, 3, "hhhh", 1)


# # 元组和列表的取值(查询)
# print(list01[1])
# print(tuple01[3])
# for index in range(len(list01)):
#     print(list01[index])
# for index in range(len(tuple01)):
#     print(tuple01[index])
# for element in list01:
#     print(element)
# for element in tuple01:
#     print(element)

# # 元组和列表切片
# print(list01[1:9])
# print(tuple01[1:])
# print(tuple01[:2])
#
# # tuple
# # tuple中寻找元素值为2的索引号
# print(tuple01.index(2))
# # tuple中查询元素值为2 的元素个数
# print(tuple01.count(1))
# # 元组根据索引号取值
# print(tuple01[3])

# list
# list中添加
print(list01)
list01.append("superzyx")
print(list01)
list02 = [1, 3, "jaishfas", True]
list01.extend(list02)
print(list01)
list01.insert(2, "hahahahahahha")
# list中删除
list01.pop(3)
print(list01)
list01.remove("superzyx")
print(list01)
# list02.clear()
# print(list02)
# del list02
# print(list02)

# list中改
list03 = [1, 2, 3, 4, 5, 6, 2]
list03.sort()
print(list03)
list03.reverse()
print(list03)
# list中查
# 查看已知元素2 ，在index=5后的index号
print(list03.index(2, 5, ))
print(list01[6])
print(list01)
print(list01.count(1))

print(list(tuple01))
print(type(list(tuple01)))

# string
# string 增
str01 = " It's my horse"
str01 = str01 + " ,baby"
print(str01)

# string 删
print(str01.lstrip("It"))
print(str01.rstrip("se"))
# 删除首尾的空格
print(str01.strip())

# string 改
print(str01.replace("my", "your"))
print(str01.replace("o", "OP", 2))      # 次数为2

# string 查
if "o" in str01:
    print("^3^")

list04 = str01.split()
print(list04)
print("dsafad: {}  {}   {}".format("ahd", 1, 4))

tuple02 = (1, 2, 3, 4, 5, 6)
print(tuple02.index(5, 1, 20))
#!/usr/bin/env python3
# ^3^coding: utf8
#
# author: superzyx
# date: 2019/08/05
# usage: study

#sd = input("input :")

# for i in range(20):
#     for j in range(20):
#         if j >=13:
#             continue
#             print(j)
#     print("i=", i)

# for i in range(1,201):
#     if i % 2 == 1 and i % 3 == 2 and i % 5 ==4 and i % 6 == 5 and i % 7 == 0 :
#         print (i)

# for i in range (1,101):
#     if i == 1 or i == 2:
#         pass
#     else :
#         for j in range (2,i):
#             if i % j == 0 :
#                 break
#             elif j == i-1 and i % j != 0:
#                 print (i)

# num01 = float(input("num01="))
# num02 = float(input("num02="))
# num03 = num01 +num02
# print(num03)

# num01 = float(input("num01="))
# num02 = float(input("num02="))
# if num01>num02:
#     num01 = str(num01)
#     num02 = str(num02)
#     print(num01 + ">" + num02)
# else:
#     num01 = str(num01)
#     num02 = str(num02)
#     print(num01 + "<=" + num02)

# num01 = int(input("num01="))
# num02 = int(input("num02="))
# max = 0
# for i in range(1,num01+1):
#     if num02 % i == 0 :
#         max = i
# print(max)

# num01 = int(input("num01="))
# num02 = int(input("num02="))
# max = num01 * num02
# # print(max)
# min = 0
# for i in range(1,max):
# #   print(i)
#     if i % num01 == 0 and i % num02 ==0 :
#         min = i
#         print(min)
#         break;

# result = 0
# for i in range(101):
#     result = result + i
# print(result)

# result = 1
# for i in range(1,11):
#     result = result * i
# print(result)

# sentence01 = "this is my house"
# sentence02 = ""
# list01 = sentence01.split(" ")
#
# print('''{} {} {} {} '''.format(list01[3], list01[2], list01[1], list01[0]))


# tuple01 = ("string", "world", 1, 2, 3, 4, 6, 9, 10)
# list01 = []
# i = 0              #列表的index
# for element in tuple01:
#     # print(type(element)==int)
#     if type(element) == int or type(element) == float:
#         list01.append(element)
# print(list01)

# list01 = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
# index = 0
# j = len(list01)
# while j > 0:
#     for i in range(j-1):
#         if list01[i] > list01[i+1]:
#             index = list01[i]
#             list01[i] = list01[i+1]
#             list01[i+1] = index
#     j -= 1
# print(list01)

# list01 = [1, 2, 3.4]
# tuple01 = (1, "jjj", 9)
# print(list01.__sizeof__())
# print(tuple01.__sizeof__())
# list01.append("zyx")
# tuple01 = tuple01 + (1,)
# print(list01.__sizeof__())
# print(tuple01.__sizeof__())
# tuple01 = tuple01 +("jajskaf", )
# list01.append("yyy")
# print(list01.__sizeof__())
# print(tuple01.__sizeof__())

list01 = [1, 2, 3, 4, 5, 6, 7]
tuple01 = (1, 2, 3, 4, 5, 6)
for element in list01:
    print(element)

tuple01 = (2, 4.445, False, "String Type")
number = tuple01.count(1)						# 统计元素1的数量
print(number)
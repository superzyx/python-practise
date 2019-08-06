#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/06
# usage:practise


# zodiac = ('猴', '鸡', '狗', '猪', '鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊')
#
# constellation = ('水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座',
#                  '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座')
#
# constellDate = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22),
#                 (7, 23), (8, 23), (9, 23), (10, 24), (11, 23), (12, 22), (12, 32))
#
#
# year = int(input("请输入你的出生年份: "))
# month = int(input("请输入你的出生月份: "))
# date = int(input("请输入你的出生日子: "))
# print(zodiac[year % 12])
#
# for index in range(len(constellDate)-1):
#     if (month, date) > constellDate[index] and (month, date) < constellDate[index + 1]:
#         print(constellation[index])
#     elif (month, date) < (1, 20):
#         print(constellation[-1])
#         break

# list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
# list02 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
# list03 = []
# list01.remove((1, 2, 3, 4, 5))
# list01.remove([6, 7])
# # print(list02.pop(3)[1])
# list03 = list(list02[3])
# list03.extend(list02[4])
# list01.extend(list03)
# print(list01)

# sen04 = input("他说：")
# if "草泥马" in sen04:
#     print(sen04.replace("草泥马", "***"))
# else:
#     print(sen04)

# list01 = []
# tuple01 = ("string", "world", 1, 2, 3, 4, 6, 9, 10)
# for element in tuple01:
#     if type(element) == int:
#         list01.append(element)
# print(list01)

# list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
# list02 = list01[:3]
# print(list02)
# for index in range(len(list01[3])):
#     list02.append(list01[3][index])
# for index in range(len(list01[4])):
#     list02.append(list01[4][index])
# print(list02)


list01 = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
for i in range(len(list01)-1):
    for j in range(len(list01)-i-1):
        if list01[j] > list01[j+1]:
            list01[j], list01[j+1] = list01[j+1], list01[j]
print(list01)



#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/06
# usage:practise


zodiac = ('猴', '鸡', '狗', '猪', '鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊')

constellation = ('水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座',
                 '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座')

constellDate = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22),
                (7, 23), (8, 23), (9, 23), (10, 24), (11, 23), (12, 22), (12, 32))


year = int(input("请输入你的出生年份: "))
month = int(input("请输入你的出生月份: "))
date = int(input("请输入你的出生日子: "))
print(zodiac[year % 12])

for index in range(len(constellDate)-1):
    if (month, date) > constellDate[index] and (month, date) < constellDate[index + 1]:
        print(constellation[index])
    elif (month, date) < (1, 20):
        print(constellation[-1])
        break

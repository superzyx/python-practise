#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/10
# usage: sort qiuckly


def sortq(list01):
    if len(list01) < 2:
        return list01
    else:
        nu = list01[0]
        listr = [i for i in list01[1:] if i > nu]
        listl = [r for r in list01[1:] if r < nu]
        return sortq(listl) + [list01[0]] + sortq(listr)
a = sortq([2, 4, 3, 0])
print(a)


betw = 0
def sortq_advance(i):
    if i == None:
        return None
    else:
        if i > betw:
            listr.append(i)
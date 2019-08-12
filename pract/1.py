#！/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/11
# usage:preview


def residual(element):
    if element % 2 == 0:
        return element


result = filter(residual, range(10))
print(list(result))
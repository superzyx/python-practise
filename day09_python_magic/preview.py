#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/16
# usage: preview last week learning


import functools
def decorate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('jj')
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@decorate
def play(a):
    b = a
    return b


a = play(4)
print(a)
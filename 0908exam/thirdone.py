#!/usr/bin/env python3
# ^3^ coding=utf-8
#
# author: superzyx
# date: 2019/09/08
# usage: the third one of exams


# 3.请使用python代码写出验证用户登录的装饰器，要求：装饰器可以接收函数的参数

import functools

def decorate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        if args[0] == 'login':
            func(*args, **kwargs)
    return wrapper

@decorate
def mkdir(k):
    print('lllll')

mkdir('login')
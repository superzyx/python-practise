#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/12
# usage: practise decorate


# import functools
# def func(function):
#     @functools.wraps(function)
#     def change(*args, **kwargs):
#         print('调用了装饰器')
#         function(*args, **kwargs)
#     return change
# @func
# def changename(*args, **kwargs):
#     print(*args, **kwargs)
#
# changename('zyx')


# import functools
#
# username = ('peter', 'zyx')
# password = {'peter': '!@#123','zyx': '123!@#'}
# def decorate(func):
#     @functools.wraps(func)
#     def add(a,b):
#         if a in username and password[a] == b:
#             func(a,b)
#             print('调用了装饰器successful')
#         else:
#             print('error!!!!')
#     return add
#
# @decorate
# def login(a,b):
#     print('这是一个登录界面')
# @decorate
# def commit(a,b):
#     print('这是一个验证界面')
#
# index = input('please input where are you go')
# user = input('use:')
# passwd = input('password:')
# if(index == 'login'):
#     login(user, passwd)
# elif(index == 'commit'):
#     commit(user, passwd)
# else:
#     print('404')


# import functools
# def decorate(func):
#     @functools.wraps(func)
#     def add(*args, **kwargs):
#         print('hhahah')
#         func(*args, **kwargs)
#     return add
#
# @decorate
# def fir(a,b):
#     print(a,b)
#
# fir('成功','了')



import functools
import time
import datetime
def decorate(func):
    @functools.wraps(func)
    def getTime(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print('{:s} took {:f} {:f} {:f}'.format(func.__name__, end, start, (end-start)))
    return getTime


def stepCount(a):
    @decorate
    def count():
        nonlocal a
        a += 1
        print(a)
        # print(a+1)
        # list01 = [(lambda x: x**6)(i) for i in range(a)]
        # print(list01)
        # return a
    return count

print("开始计步，初始值：10")
step = stepCount(10)
# print(step())
# print(step())
# print(step())
step()
step()
step()


# first = time.time()
#
# listA = [x for x in range(10)]
# print(listA)
#
# end = time.time()
# print('时间差: {:f}'.format((end - first)*10000))
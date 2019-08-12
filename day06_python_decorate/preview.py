#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/12
# usage: preview


# import functools
# import datetime
# name = ('Tom', 'Bob', 'zyx')
# password = {'Tom': '!@#123', 'Bob': '123!@#', 'zyx': '456$%^'}
# def web(func):
#     @functools.wraps(func)
#     def wrapper(username, passwd):
#         if username in name and passwd == password[username]:
#             print('卧槽，成功了')
#             func(username, passwd)
#         else:
#             print('gun')
#     return wrapper
#
# @web
# def login(username, passwd):
#     log = '{} username:{} login in successfully!'.format(datetime.datetime.now(), username)
#     print(log)
# @web
# def check(username, passwd):
#     log = '{} username:{} check out successfully!'.format(datetime.datetime.now(),username)
#     print(log)
#
# module = input('where do you want to go ?')
# username = input('please input your name:')
# passwd = input('please input your name:')
# if module == 'login':
#     login(username,passwd)
# elif module == 'check':
#     check(username, passwd)
# else:
#     print('404')


import functools
import time
import datetime

def countTask(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print('{} {} took {:f}'.format(datetime.datetime.now(), func.__name__, (end - start)))
    return wrapper


def stepCount(n):
    @countTask
    def count():
        nonlocal n
        n += 1
        print(n)
    return count

i = int(input('开始计步，初始值：'))
step = stepCount(i)
step()
step()
step()

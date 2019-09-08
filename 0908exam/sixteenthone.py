#!/usr/bin/env python3
# ^3^ coding=utf-8
#
# author: superzyx
# date: 2019/09/08
# usage: the sixteenth one of exams


class Website:
    def __init__(self):
        pass
    def login(self):
        print('login in website successfully!!!!!!!!')
    def regist(self):
        print('regist in website successfully!!!!!!!!!')
    def welcome(self):
        print('welcome to our website!!!!!!!!!!')


whereinfo = input('where do you want to go?')
web = Website()
if hasattr(web, whereinfo):
    method = getattr(web, whereinfo)
    method()
#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/14
# usage: hasattr getattr setattr delattr


class Website():
    VERSION = 'web0.1'
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def login(self):
        print('{}/{} login page'.format(self.url, self.token))

    def logout(self):
        print('{}/{} logout page'.format(self.url, self.token))

    @staticmethod
    def welcome(content):
        print('hhhh ,, {}'.format(content))

url = input('url = ')
token = input('token = ')
there = Website(url, token)
# there.login()
if hasattr(there, token):
    web = getattr(there, token)
    print(type(token))
    if token == 'welcome':
        web('kkasdas')
    else:
        web()




#
# class Webopera:
#
#     VERSION = '1.0'
#
#     def __init__(self, url, token):
#         self.url = url
#         self.token = token
#
#     def login(self):
#         print('{}/{} login page'.format(self.url, self.token))
#
#     def logout(self):
#         print('{}/{} logout page'.format(self.url, self.token))
#
#     @staticmethod
#     def welcome(content):
#         print('''Welcome to Webopera
#         {}'''.format(content))
#
# def opera(url, token):
#     web = Webopera(url=url, token=token)
#     if hasattr(web, token):
#         method = getattr(web, token)
#         if token == 'welcome':
#             method('version: @{}'.format(Webopera.VERSION))
#         else:
#             method()
#     else:
#         print('[ERROR] {} method not found in Webopera'.format(token))
#
# opera('www.qfcloud.com', 'login')
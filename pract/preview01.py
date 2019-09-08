#!/usr/bin/env python3
#
# author:superzyx
# date: 2019/09/07
# usage: preview python


# import paramiko
#
# private = paramiko.RSAKey.from_private_key_file('$HOME/.ssh/id_rsa')
# transport = paramiko.Transport(('192.168.161.34', 22))
# transport.connect(username='root', pkey=private)
# client = paramiko.SSHClient()
# client._transport = transport
#
# stdin, stdout, stderr = client.exec_command(command='', timeout=1)
# transport.close()
#
#
# private = paramiko.RSAKey.from_private_key_file('')
# transport = paramiko.Transport(('192.168.161.34', 22))
# transport.connect(username='root', pkey=private)
# sftp = paramiko.SFTPClient.from_transport(transport)
#
# sftp.get(remotepath='', localpath='')
# sftp.put(localpath='', remotepath='')
#
# transport.close()


# import pymysql
#
# client = pymysql.connect(
#     host='',
#     port=3306,
#     user='superzyx',
#     password='ZYx..(12138)',
#     db='test'
# )
# cursors = client.cursor()
#
# sql = ''
# cursors.execute(sql)
# stdout = cursors.fetchall()
#
# client.commit()
# client.close()


import redis

pool = redis.ConnectionPool(host='', port=6379, db=0)
client = redis.Redis(connection_pool=pool)

client.hset(name='', key='', value='')
client.flushdb(11)
client.flushall()
client.hmset(name='', mapping={})
#
# import redis.sentinel
# sent = redis.sentinel.Sentinel([('192.168.161.34',26379)])
# master = sent.discover_master('mymaster')


# import subprocess
#
# a = subprocess.Popen('', shell=True, stdout=subprocess.PIPE)
# print(a.stdout.read().encode('utf-8'))

# import psutil
#
# a = psutil.cpu_times_percent(interval=1)
# b = psutil.virtual_memory()
# c = psutil.disk_usage('/')
# d = psutil.pids()
# e = psutil.Process(120)
# f = psutil.net_if_stats()
# g = psutil.net_connections(kind='inet4')[0].fd
# j = psutil.net_io_counters()
#
# print(j)

# import re
# str = 'ajfgaf.safa/'
# re.split('./s', str)
# zz = '[ah][jk]'
# a = re.findall(zz , str)
# print(a)
# b = re.compile(zz)
# c = b.findall(str)
# d = b.sub('', str, 2)
# f = b.search(str)
# print(f)

# import logging.config
#
# logging.config.fileConfig('')
# logger = logging.getLogger('')
# logger.error()

#
# class Ball:
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def createBall(cls):
#         return cls(name='zyx')
#
#     def __call__(self, *args, **kwargs):
#         print(self.name)
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
# class Basketball(Ball):
#     def __init__(self, name, size):
#         super(Basketball, self).__init__(name)
#         self.size = size
#
# ball = Ball.createBall()
# ball()

# import yagmail
#
# client = yagmail.SMTP(user='superzyx@163.com',password='',host='smtp.163.com')
# con=[]
# client.send(to=[''],subject='',contents=con)

# import requests
#
# api = ''
# data={
#
# }
# requests.post(url='',data=, headers=)


# import openpyxl
#
# file = openpyxl.load_workbook('')
# file01 = openpyxl.Workbook('')
# sheet = file['Sheet']
# sheet.append()
# file.save('')

# import fnmatch
# import os
#
# # images = ['*.py', '*.png', '*.jpeg', '*.tif', '*.tiff']
# # matches = []
# for dirPath, dirNames, fileNames in os.walk(os.getcwd()):
# #     for picture in images:
# #         for filename in fnmatch.filter(fileNames, picture):
# #             matches.append(os.path.join(dirPath, filename))
# #     print(matches)
#
#     print(dirPath)
#     print(dirNames)
#     print(fileNames)



# import functools
#
# def decorate(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('996')
#         func(*args, **kwargs)
#     return wrapper
#
# @decorate
# def tun(i):
#     print(i)
#
# tun(9)

#
# import random
# list01 = [1, 7 ,3]
# random.shuffle(list01)
# print(list01)


# class Yull:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "help:::"
#     def __call__(self, *args, **kwargs):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
# class Jjj():
#     def __init__(self):
#         pass
#     def cl(self, aaa):
#          aaa.name = "zyx"
#          print(aaa.name)
#
# a = Yull('op')
# b = Jjj()
# b.cl(a)

import psutil

a = psutil.cpu_times_percent(interval=1)
b = psutil.virtual_memory()
c = psutil.disk_usage('/')

print(a)
print(b)
print(c)
#！/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/11
# usage:preview


# def residual(element):
#     if element % 2 == 0:
#         return element


# result = filter(residual, range(10))
# print(list(result))
import psutil


# import requests
# #
# # reponse = requests.get(url= 'https://baidussssss.com')

# for iny in (it for it in range(10)):
#     print(iny)
#
# pp = 'asdfasdgf'
# # a = pp.rstrip('f')
# # print(a)
# a = pp.replace('as', 'AS', 2)
# print(a)
#
# okc = {'name': 'zyx', 'sex': 'man'}
# okc.update([('name','zyx01')])
# print(okc)

# set01 = {1, 3 ,45}
# list01 = [90, 6976, 1734]
# set01.update(list01)
# print(set01)

# fig = lambda x,y: x* y
# a = fig(8, 9)
# print(a)

#
# def func01():
#     print('llasda')
#     def func02():
#         print('kkkkkkkkk')
#


# func01()


# import random
#
# num = ''
# for i in range(5):
#     a = random.choice([str(random.randint(0,9)),chr(random.randint(65,90))])
#     num = num + a

#
# import functools
# import random
#
#
#
# def pict():
#     num = ''
#     for i in range(5):
#         a = random.choice([str(random.randint(0,9)),chr(random.randint(65,90))])
#         num = num + a
#     return num
#
#
# def decorate(func):
#     @functools.wraps(func)
#     def wrapper(cd):
#         num = pict()
#         print(num)
#         password = input('请输入验证码：')
#         if password.upper() == num:
#             func(cd)
#     return wrapper
#
# @decorate
# def println(cd):
#     print(cd)
#
# println('sdfhaoweh')
#
# dict_ip = {'192.168.161.78': 789, 'ahsdgf': 934, 'ashdfuag': 32}
# dict01 = dict(sorted(dict_ip.items(), key = lambda x: x[1], reverse=True))
# print(dict01)


# class Info:
#     def __init__(self, name, sex):
#         self.name= name
#         self.sex =sex
#
#     @classmethod
#     def createinfo(cls, name, sex):
#         return cls(name, sex)
#
#
#
# # class info_01(Info):
# #     def __init__(self, name, sex, age):
#
# ip = Info.createinfo('1', 'isdf')

# class List:
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#     def __call__(self, *args, **kwargs):
#         print('asdkjfhakjdfabfweugfjkwef')
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
# class Piot(List):
#     def __init__(self, name, sex, age):
#         super(Piot, self).__init__(name, sex)
#         self.age = age
#     @classmethod
#     def createPiot(cls, name, sex, age):
#         return cls(name, sex, age)
#
#     @staticmethod
#     def welcome(content):
#         print('Welcome to {}'.format(content))
#
#     def changelogin(self,con):
#         con.token = 'regist'
#
# class Web(List):
#     def __init__(self, name, sex, url, token):
#         super(Web, self).__init__(name, sex)
#         self.url = url
#         self.token = token
#
#     @classmethod
#     def createWeb(cls, url, token):
#         return cls(name='zyx', sex='man', url=url, token=token)
#
#     def login(self):
#         print('login successfully!!!!')
#
#     def regist(self):
#         print('regist successfully!!!!')
#
# url = input('请输入url:')
# token = input('请输入token:')
#
# web = Web.createWeb(url, token)
# poit = Piot('zyx', 'man', 89)
#
# if hasattr(web, token):
#     poit.changelogin(web)
#     website = getattr(web, web.token)
#     website()
#
#
#
#     list01 = List('zyx','ashd')
#     list01()
# if hasattr(poit, token):
#     piot = getattr(poit, token)
#     piot('zyx')




# url = input('url=')
# var01 = __import__('source.website', fromlist=True)
#
# if hasattr(var01, url.split('/')[-1]):
#     ap = getattr(var01, url.split('/')[-1])
#     ap()

# import fnmatch
#
# a = fnmatch.fnmatch('zyx.txt', '*.txt')
# print(a)
# list01 = ('zyx.txt', 'yy.py', 'kuh.txt')
# list02 = fnmatch.filter(list01, '*.txt')
# print(list02)

# import logging.config
#
# logging.config.fileConfig('./log.conf')
# logger = logging.getLogger('rotatehandle')
# logger.error()
#
#
# import subprocess
#
# subprocess.run('ls /', shell=True)
# subprocess.run(['ls','/'])
# df = subprocess.Popen('ls /', shell=True, stdout=subprocess.PIPE)
# sf = subprocess.Popen('grep paramiko', shell=True, stdin=df.stdout, stdout=subprocess.PIPE)
# print(sf.stdout.read().encode('utf-8'))


# import re
#
# str = 'jfjdf.sadf/asdf,adfra'
# a = re.split('[./,]', str)
# print(a)


# import os
# import fnmatch
# import re
#
# def check(i):
#     list_dir = os.listdir(i)
#     print(list_dir)
#     for path in list_dir:
#         if os.path.isdir(path):
#             check(os.path.join(os.getcwd(),path))
#         print(os.path.join(os.getcwd(),path))
#
# check(os.getcwd())

import paramiko
import psutil

# private = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
#
# transport = paramiko.Transport(('192.168.161.13', 22))
# transport.connect(username='root', pkey=private)
# client = paramiko.SSHClient()
# client._transport = transport
#
# stdin, stdout, stderr = client.exec_command(command='ls /', timeout=1)
#
# print(stdout.read().decode('utf-8'))
# transport.close()


# private = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
#
# transport = paramiko.Transport(('192.168.161.13', 22))
# transport.connect(username='root', pkey=private)
#
# sftp = paramiko.SFTPClient.from_transport(transport)
#
# sftp.get()
# sftp.put()
#
# transport.close()



# cpu = psutil.cpu_times_percent(interval=1)
# print(cpu)
# user = cpu.user
# system = cpu.system
# idle = cpu.idle
#
# memory = psutil.virtual_memory()
# print(memory)
# used = memory.used
#
# disk = psutil.disk_usage('/')
# print(disk)
#
# net1 = psutil.net_io_counters()
# print(net1)
# net2 = psutil.net_connections(kind='inet4')
# print(net2)
# net3 = psutil.net_if_stats()
# print(net3)
#
# psutil.pids()
# psutil.process(1)


# import pymysql
#
# client = pymysql.connect(
#     host='192.168.161.34',
#     port=3306,
#     user='superyzx',
#     password='ZYx..(12138)',
#     cursorclass=pymysql.cursors.DictCursor
# )
# cursors = client.cursor()
# sql=''
# cursors.execute()
# cursors.fetchall()
# client.close()


# import redis
#
# pool = redis.ConnectionPool(host='192.168.161.13', port=6379, db=0)
# client = redis.Redis(connection_pool=pool)
#
# client.hset('list', 'name', 'zyx')
# client.hmset('list',{('sex','man'), ('age', 90)})
# client.hget('list', 'name')
# client.hmget('list', 'name', 'sex', 'age')
# client.hgetall('list')
# client.hdel('list', 'name')
# client.delete('list')
#
#
# from redis import sentinel
# sentinel = sentinel.Sentinel([('192.168.161.13', 26379)])
#
# master = sentinel.discover_master('mymaster')

#
# import yagmail
#
# client = yagmail.SMTP(
#     user='superzyx12138@163.com',
#     password='',
#     host='smtp.163.com'
#
# )
# contents = [
#     '',
#     ''
# ]
#
# client.send(
#     to=['',''],
#     subject='',
#     contents=contents,
#
# )


# import requests
# import json
#
# api = 'https://oapi.dingtalk.com/robot/send?access_token=b6334a2f5283764f80a31064e11c954c87474895161689ff41fb9e9a6328b148'
#
# header = {'Content-Type': 'application/json'}
# data = {
#     "msgtype" : "text",
#     "text": {
#         "content": "测试发送测试信息至钉钉群"
#     },
#     'at': {
#         'atMobiles': [
#             '15222401953',
#             '185xxxx8271'
#         ]
#     },
#     'isAtAll': 'false'
# }
#
# senddata = json.dumps(data).encode('utf-8')
# requests.post(url=api, data=senddata, headers= header)


import openpyxl

a = openpyxl.load_workbook('')
sheet = a.create_chartsheet('jhad', 0)
sheet01 = a['Sheet']

sheet['A2']= ''
sheet01.append(['asdssda','ajfh'])

a.save('')
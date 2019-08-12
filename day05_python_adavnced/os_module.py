#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/09
# usage: OS module learning


import os

print(os.listdir(os.getcwd()))
a= os.getcwd()
print(a)
os.chdir('D:\PycharmProjects')
print(os.getcwd())
print(os.listdir(os.getcwd()))
os.chdir('D:\PycharmProjects\python-practise\day05_python_adavnced')

print(os.path.isdir('.\os_module.py'))
print(os.path.isfile('.\os_module.py'))
b = os.path.getsize('.')
print(b)

print(os.path.abspath('os_module.py'))
c = os.path.split(os.path.abspath('os_module.py'))
print(c)
d = os.path.splitext('os_module.py')
print(d)
print(os.path.join('a', 'b'))
print(os.path.basename(os.path.abspath('os_module.py')))
os.remove('D:\PycharmProjects\python-practise\pract\jj.txt')



#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/15
# usage: many_inherit


# class A:
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#
# class B(A):
#     def __init__(self, name, sex, age):
#         A.__init__(self,name,sex)
#         # self.name = name
#         # self.sex = sex
#         self.age = age
#
# class C(A):
#     def __init__(self, name, sex, hobby):
#         A.__init__(self,name,sex)
#         # self.name = name
#         # self.sex = sex
#         self.hobby = hobby
# class D(B,C):
#     def __init__(self, name, sex, age, hobby):
#         B.__init__(self,name,sex,age)
#         C.__init__(self,name,sex,hobby)
#
# d = D('hh',1,1,1)

class Father:
    def __init__(self,name):
        self.name = name

    @property
    def fightSon(self):
        return '{} fight !!'.format(self.name)

    @fightSon.setter
    def fightSon(self, name):
        self.name = name

    @fightSon.deleter
    def fightSon(self):
        print('hehe')

class Son(Father):
    def __init__(self,name,nu):
        super(Son, self).__init__(name)
        self.nu = nu

    def jj(self):
        print('llll')

son = Son('狗子',1)
son.fightSon = '大明'
print(son.fightSon)

if hasattr(Father, son.fightSon):
    print('ahdsja')
else:
    print('kkkk')


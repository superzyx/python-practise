#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/13
# usage: class practise


# class Box():
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height
#     def getVolumn(self):
#         volumn = self.length * self.width * self.height
#         return volumn
#
# paperBox = Box(1,2,3)
# print(paperBox.getVolumn())
# print(paperBox.length)


# class Box:
#     """
#     class: Box
#     usage: 能够生成多个盒子, 并获得盒子的面积
#     """
#     VERSION = 'copyright@2019 version 2.0'
#
#     def __init__(self, color):
#         self.length = 1
#         self.width = 1
#         self.height = 1
#         self.__color = color
#
#     def getArea(self):
#         print(self.VERSION)
#         sideArea = self.length * self.height + self.width * self.height
#         bottomArea = self.length * self.width
#         return (sideArea + bottomArea) * 2
#
#     def getColor(self):
#         return self.__color
#
#
# paperBox = Box('yellow')
# pArea = paperBox.getArea()
# print(pArea)
# print(paperBox.getColor())
# ironBox = Box('yellow')
# ironBox.length = 20
# ironBox.width = 15
# ironBox.height = 4
# iArea = ironBox.getArea()
# print(iArea)
# print(Box.VERSION)
# # print(help(Box))










# class Games:
#     def __init__(self, blood, *args):
#         self.blood = blood
#         self.args = args
#
#     @classmethod
#     def createPlayer(cls, name, blood, *args):
#         return cls(name, blood, *args)
#
#
# class Zombie(Games):
#     def __init__(self, blood, *args):
#         super(Zombie, self).__init__(blood, *args)
#         self.args = args
#
#     @staticmethod
#     def bite():
#         print('咔哧')
#
#     @staticmethod
#     def move(stepCount=0):
#         stepCount += 1
#         return stepCount
#
#     def jump(self):
#         self.args += 2
#         return self.args
#
#     def attack(self, stance):
#         stance.blood -= 1
#
#
# class Arms(Games):
#     def __init__(self, blood, *args):
#         super(Arms, self).__init__(blood, *args)
#         self.args = args
#
#     def attack(self, zombie):
#         zombie.blood -= 1
#
#
# zombie = Zombie(100)
# arms = Arms(100)
#
# for step in range(100):
#     if step % 10 == 0:
#         Games.createPlayer('太阳', 20)
#         print('your have created sunshine')
#     if zombie.move(step) > 9:
#         zombie.attack(arms)
#         zombie.bite()
#     arms.attack(zombie)
#     if zombie.blood == 0:
#         print('zombie is die !')
# print(arms.blood)


class Nginx_operate:
    __con = 90

    def __init__(self, filepath):
        print('2')
        self.filepath = filepath

    @classmethod
    def createNginx(cls,filepath):
        print('1')
        print(cls.__con)
        return cls(filepath)

    # @staticmethod
    # def

    def get_count(self):
        list01 = []
        with open(file=self.filepath, mode='r', encoding='utf8') as file01:
            for item in file01.readlines():
                list01.append(item.split()[0])
        print('PV = {}'.format(len(list01)))
        print('UV = {}'.format(len(set(list01))))

    def get_status(self):
        dict01 = {}
        with open(file=self.filepath, mode='r', encoding='utf8')as file02:
            for item in file02.readlines():
                if item.split()[8] in dict01.keys():
                    dict01[item.split()[8]] += 1
                else:
                    dict01[item.split()[8]] = 1
        print(dict01)

    def hot_resource(self):
        dict02 = {}
        with open(file=self.filepath, mode='r', encoding='utf8')as file03:
            for item in file03.readlines():
                if item.split()[6] in dict02.keys():
                    dict02[item.split()[6]] += 1
                else:
                    dict02[item.split()[6]] = 1
        print(dict02)

idr = Nginx_operate.createNginx('../day03_python_dict,set/reading/access_log')
idr.hot_resource()
idr.get_count()

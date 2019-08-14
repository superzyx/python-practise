#!/usr/bin/env python3
# ^3^ coding= utf8
#
# author: superzyx
# date: 2019/08/14
# usage: practise inherit


class Ball:
    def __init__(self, radius, color):
        self.radius = radius
        self.__color = color


class RoundBall(Ball):
    def __init__(self, radius, color, size):
        super(RoundBall,self).__init__(radius, color)
        self.__size = size

    @classmethod
    def createball(cls, radius, color,size):
        return cls(radius, color, size)

    @property
    def printlm(self):
        print('size = ', self.__size )
        # print(self.__color)

    @printlm.setter
    def printlm(self, size):
        self.__size = size


    @printlm.deleter
    def printlm(self):
        print('删了')




basketball = RoundBall.createball(1,1,1)
basketball.printlm = [8, 9]
basketball.printlm
print(basketball.radius)

print(isinstance(basketball, Ball))

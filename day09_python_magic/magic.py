#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/15
# usage: magic function called


# import random
#
#
# class Game:
#     def __init__(self, blood, attack):
#         self.blood = blood
#         self.attack = attack
#
# class Player(Game):
#     buf = random.randint(0,100)
#     def __init__(self, blood, attack, bloodget):
#         super(Player, self).__init__(blood, attack)
#         self.bloodget = bloodget
#
#     def attackhim(self, instance):
#         instance.blood -= self.attack + self.buf
#         self.blood += (self.attack + self.buf) * self.bloodget
#
#
# person_horse = Player(500, 59, 0.2)
# bird_man = Player(200, 90, 0.6)
#
# for i in range(100):
#     if i % 2 == 0:
#         person_horse.attackhim(bird_man)
#         if bird_man.blood <= 0:
#             print('人马赢了')
#             break
#         print('人马生命值：{}'.format(person_horse.blood))
#         print('鸟人生命值：{}'.format(bird_man.blood))
#     else:
#         bird_man.attackhim(person_horse)
#         print('人马生命值：{}'.format(person_horse.blood))
#         print('鸟人生命值：{}'.format(bird_man.blood))
#         if person_horse.blood <= 0:
#             print('鸟人赢了')
#             break


# class Ball:
#     def __init__(self, blood):
#         self.blood = blood
#
# class Basketball(Ball):
#     def __init__(self, blood):
#         super(Basketball,self).__init__(blood)
#
#     def play_basketball(self):
#         print('playe')
#
# basket = Basketball(78)
# basket01 = Basketball('akd')
# basket.play_basketball()


class Ball:
    def __init__(self, radius, size):
        self.radius = radius
        self.size = size


class Basketball(Ball):
    def __init__(self, radius, size, color):
        super(Basketball, self).__init__(radius, size)
        self.color = color
    def playBasketball(self):
        print('ball is {}'.format(self.color))

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    def __call__(self, color):
        self.color = color
        print(self.color)

basketball = Basketball(1,1,1)
football = Basketball(8,8,8)
if id(football) == id(basketball):
    print('yes')
football('2b')
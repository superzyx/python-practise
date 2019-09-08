#!/usr/bin/env python3
# ^3^ coding= utf8
#
# author: superzyx
# date: 2019/08/19
# usage: random function


import random

tuple01 = (0, 1, 2, 3)
a = random.choice(tuple01)
print(a)
random.shuffle(tuple01)
print(tuple01)

# m = 1
# while m != 9:
#     m = random.uniform(1,9)
#     print(m)
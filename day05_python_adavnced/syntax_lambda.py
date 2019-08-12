#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author:superzyx
# date:2019/08/09
# usage: OS module learning


d = {'mike': 10, 'lucy': 2, 'ben': 30}
d = dict(sorted(d.items(), key=lambda list: list[1], reverse=True))
print(d)
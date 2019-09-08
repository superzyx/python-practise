#!/usr/bin/env python3
# ^3^ coding=utf-8
#
# author: superzyx
# date: 2019/09/08
# usage: the twentieth one of exams


# 19.初始化类的属性

class Ball:
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

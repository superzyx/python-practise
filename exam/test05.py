#!/usr/bin/env python3
# coding=utf8
#
# author:superzyx
# date:2019/08/09
# usage:exam


def stepCount(count):
    def stepcount():
        count +=1
    return stepCount


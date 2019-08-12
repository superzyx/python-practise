#!/usr/bin/env python3
# coding=utf8
#
# author:superzyx
# date:2019/08/09
# usage:exam


ips = {'192.168.161.10': 13, '39.100.110.135': 8, '1.1.1.1': 11, '8.8.8.8': 5}

ips = dict(sorted(ips.items(), key=lambda x:x[1], reverse=True))
print(ips)
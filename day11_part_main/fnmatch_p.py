#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/19
# usage: os, fnmatch


import fnmatch
import os

jj = ('*.txt', '*.ll')
for dirpath, dirname, filename in os.walk('filedir'):
    print(dirpath, dirname, filename)
    for j in jj:
        for name in filename:
            if fnmatch.fnmatch(name, j):
                print(name)

import sys

sys.exit(9)




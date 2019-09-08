#!/usr/bin/env pyhton3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/26
# usage: monitor action


# from transport_info.transport_info import putfile
from put_files.source.transport_info import getfile
from put_files.source.transport_info import exefile
from put_files.source.connect_mysql import get_hostname

import time

path = '/root/.ssh/id_rsa'
hostname = get_hostname()
print(hostname)
for name in hostname:
    try:
        exefile(name[0], path)
        print(111111111111111111111111111111111)
        time.sleep(5)
        getfile(name[0], path)
        print(222222222222222222222222222222222222)
    except Exception as error:
        print(error)






#!/usr/bin/env pyhton3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/26
# usage: monitor action


from put_files.source.transport_info import putfile
from put_files.source.connect_mysql import get_hostname

path = '/root/.ssh/id_rsa'
hostname = get_hostname()
print(hostname)
for name in hostname:
    try:
        putfile(name[0], path)
    except Exception as error:
        print(error)

#!/usr/bin/env pyhton3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/26
# usage: ps


from source import getinfo_mathod
from source.getinfo_mathod import write_into_json
from source.connect_mysql import save_info


cpu, memory, disk =getinfo_mathod.getinfo()
save_info(cpu, memory, disk)
write_into_json(cpu, memory, disk)
if cpu > 80:
    print('cpu 报警了！！！')
if memory > 90:
    print('内存报警了！！！')
if disk > 85:
    print('磁盘报警了！！！')


#!/usr/bin/env pyhton3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/26
# useage: the method of getting information


import psutil
import json

def getinfo():
    cpu = psutil.cpu_times_percent(interval=1)
    cpuinfo = cpu.user
    memory = psutil.virtual_memory()
    memoryinfo = memory.percent
    disk = psutil.disk_usage('/')
    diskinfo = disk.percent
    return cpuinfo,memoryinfo,diskinfo


def write_into_json(cpu, memory, disk):
    dict={
        'cpuinfo': cpu,
        'meminfo' : memory,
        'diskinfo' : disk
    }
    with open(file='/mnt/0826_project/cpu.json', mode='a', encoding='utf-8')as file:
        file.write(json.dumps(dict))

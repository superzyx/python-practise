#!/usr/bin/env pyhton3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/26
# usage: connect mysql


import pymysql
import time
import subprocess

def save_info(cpuinfo, memoryinfo, diskinfo):
    client = pymysql.connect(
        host='192.168.161.34',
        port=3306,
        user='superzyx',
        password='ZYx..(12138)',
        db='Test'
    )
    cursors = client.cursor()
    name = subprocess.Popen('hostname', shell=True, stdout=subprocess.PIPE)
    sql = "insert into server_info values ({},'{}','{}','{}','{}');"
    cursors.execute(sql.format(int(time.strftime('%Y%m%d%H%M%S')), name.stdout.read().decode('utf-8'), str(cpuinfo)+'%', str(memoryinfo)+'%', str(diskinfo)+'%'))


    client.commit()
    client.close()

def get_hostname():
    client = pymysql.connect(
        host='192.168.161.34',
        port=3306,
        user='superzyx',
        password='ZYx..(12138)',
        db='Test'
    )
    cursors = client.cursor()
    sql = 'select serverip from serverid'
    cursors.execute(sql)
    hostname = cursors.fetchall()
    client.commit()
    client.close()
    return hostname

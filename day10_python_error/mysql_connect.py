#!/usr/bin/env python3
# ^3^ coding= utf8
#
# author: superzyx
# date: 2019/08/19
# usage: connect mysql
import json

import pymysql

def queryDB(uid):
    def load(user='root', password='ZYx..(12138)'):
        connection = pymysql.connect(host='192.168.161.6',
                                     user='root',
                                     password='ZYx..(12138)',
                                     db='mysql')
        return connection

    # info = {}.fromkeys('email', 'passwd')
    with load().cursor() as cursor:
        sql = "select * from mysql.user"
        cursor.execute(sql.format(uid))
        result = cursor.fetchall()
    return result

data = queryDB(30)
data01 = json.loads(data)
print(data01)

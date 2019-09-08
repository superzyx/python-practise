#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/09/01
# usage: Analysis the data of logger


import requests
import yagmail
import json

class Analysis():
    def __init__(self):
        pass

    @staticmethod
    def callding(content, token='2d42f1b28f99388f63482bda247d33fb3010a2576c9b6ff2b74e191752d1d509'):
        '''
        call 110 through ding
        :param content:
        :param token:
        :return:
        '''
        api = ''.format(token)
        header = {'Content-Type': 'application/json'}
        data = {
            'msgtype': 'text',
            'text':{
                'content': content
            },
            'at':{
                'atMobiles':[
                    '15180451886'
                ]
            },
            'isAtAll': 'false'
        }
        senddata = json.dumps(data).encode('utf-8')
        requests.post(url=api, data=senddata, headers=header)

    @staticmethod
    def email(contents):
        '''
        send email
        :param contents:
        :return:
        '''
        client = yagmail.SMTP(user='superzyx12138@163.com', password='superzyx12138', host='smtp.163.com')
        content=contents
        client.send(to=['2271958554@qq.com'], subject='报警了', contents=content)

    @staticmethod
    def puv(path='/mnt/access.log'):
        '''
        get pv, uv from access.log
        :param path:
        :return:
        '''
        list_pv = []
        with open(file=path, mode='r', encoding='utf-8')as file:
            for con in file:
                list_pv.append(con.split()[0])
                pv = len(list_pv)
                uv = len(set(list_pv))
        return pv, uv

    @staticmethod
    def status(path='/mnt/access.log'):
        '''
        get status code from access.log
        :param path:
        :return:
        '''
        status_code = ('200', '301', '400', '404', '409', '499', '500', '502', '504', '505')
        list_source = {}.fromkeys(status_code)
        for code in status_code:
            list_source[code] = 0
        with open(file=path, mode='r', encoding='utf-8')as file:
            for con in file:
                if con.split()[8] in status_code:
                    # list_source.setdefault(con.split()[8], 0)
                    list_source[con.split()[8]] += 1
        return list_source

    @staticmethod
    def top(path='/mnt/access.log'):
        '''
        get top 10 from access.log
        :param path:
        :return:
        '''
        list_top = {}
        with open(file=path, mode='r', encoding='utf-8')as file:
            for con in file:
                list_top.setdefault(con.split()[0], 0)
                list_top[con.split()[0]] += 1
            dict_top = dict(sorted(list_top.items(), key=lambda x: x[1], reverse=True)[:10])
        return dict_top

    def analysis(self, path):
        '''
        calling 110 within what was happened
        :param path:
        :return:
        '''
        with open(file=path, mode='r', encoding='utf-8')as file:
            for con in file:
                try:
                    if float(con.split()[2].strip('%')) > 80:
                        self.callding('cpu爆炸了')
                        self.email('cpu爆炸了')
                    if float(con.split()[3].strip('%')) > 80:
                        self.callding('内存爆炸了')
                        self.email('内存爆炸了')
                    if float(con.split()[4].strip('%')) > 80:
                        self.callding('磁盘爆炸了')
                        self.email('磁盘爆炸了')
                except Exception as error:
                    print('日志错误！！！',error)

    def writelog(self,hostname):
        '''
        write in log
        :param hostname:
        :return:
        '''
        pv, uv = self.puv()
        status = self.status()
        top = self.top()
        data = {'pv': pv, 'uv': uv, 'status': status, 'top': top}
        json.dump(data, '/mnt/web{}.log'.format(hostname))

import paramiko

private = paramiko.RSAKey.from_private_key_file('')
transport = paramiko.Transport(('192.168.161.10', 22))
transport.connect(username='',pkey=private)
client = paramiko.SSHClient()
client._transport = transport

sftp = paramiko.SFTPClient.from_transport(transport)
client.close()

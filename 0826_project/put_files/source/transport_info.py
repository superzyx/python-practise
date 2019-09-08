#!/usr/bin/env pyhton3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/26
# usage: put and get


import paramiko
import os

def putfile(hostname, path):
    private = paramiko.RSAKey.from_private_key_file(path)
    transport = paramiko.Transport(hostname, 22)
    transport.connect(username='root', pkey=private)
    sftp = paramiko.SFTPClient.from_transport(transport)

    name = os.listdir('/mnt/0826_project/put_files')

    for rname in name:
        filename = os.path.join('/mnt/0826_project/put_files', rname)
        if os.path.isdir(filename):
            for i in os.listdir(filename):
                ifilename = os.path.join(filename, i)
                print(ifilename)
                sftp.put(localpath=ifilename, remotepath=ifilename)
                print(1)
        else:
            print(filename)
            sftp.put(localpath=filename, remotepath=filename)
            print(1)

    # sftp.put('/mnt/0826_project/put_files/get_info.py', '/mnt/kkk21.py')

    transport.close()

def getfile(hostname, path):
    private = paramiko.RSAKey.from_private_key_file(path)

    transport = paramiko.Transport((hostname, 22))
    transport.connect(username='root', pkey=private)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.get('/mnt/0826_project/cpu.json','/mnt/0826_project/cpu.json')

    transport.close()

def exefile(hostname, path):
    private = paramiko.RSAKey.from_private_key_file(path)
    transport = paramiko.Transport((hostname, 22))
    transport.connect(username='root', pkey=private)
    client = paramiko.SSHClient()
    client._transport = transport
    print('exefile 开始执行')
    client.exec_command('python3.7 /mnt/0826_project/put_files/get_info.py')
    print('exefile 执行成功')

    client.close()



#!/usr/bin/env bash
# ^3^ coding= utf8
#
# author: superzyx
# date: 2019/08/21
# usage: passwd transport connect server


# import paramiko
#
#
# private = paramiko.RSAKey.from_private_key_file('C:\\Users\\22719\\.ssh\\id_rsa')
# transport = paramiko.Transport(('192.168.161.24', 22))
# transport.connect(username='root',pkey=private)
# client = paramiko.SSHClient()
# client._transport = transport
#
# stdin ,stdout, stderr = client.exec_command('cat /etc/shadow', timeout=1)
# print(stdout.read().decode('utf-8'))
#
# transport.close()

# import paramiko
#
# private = paramiko.RSAKey.from_private_key_file('C:\\Users\\22719\\.ssh\\id_rsa')
# transport = paramiko.Transport(('192.168.161.24',22))
# transport.connect(username='root',pkey=private)
# # client = paramiko.SSHClient()
# # client._transport = transport
#
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.put(localpath='', remotepath='')
#
# transport.close()


import paramiko


private = paramiko.RSAKey.from_private_key_file('C:\\Users\\22719\\.ssh\\id_rsa')
transport = paramiko.Transport(('192.168.161.24',22))
transport.connect(username='root', pkey=private)
client = paramiko.SSHClient()
client._transport = transport

client.exec_command('echo "zyx can do it!" >>/mnt/zyx.txt',timeout=1.02)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get('/mnt/zyx.txt','.\\1.txt')

transport.close()
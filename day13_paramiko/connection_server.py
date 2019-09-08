#!/usr/bin/env bash
# ^3^ coding=utf8
#
# author:superzyx
# date: 2019/08/21
# usage: connection server check info


# import paramiko
#
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(
#     hostname='192.168.161.24',
#     port=22,
#     username='root',
#     password='1'
# )
#
# stdin, stdout, stderr = client.exec_command(command='ls ',timeout=1)
# print(stdout.read().decode('utf=8'))
#
# client.close()


import paramiko

private = paramiko.RSAKey.from_private_key_file("C:\\Users\\22719\\.ssh\\id_rsa")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname='192.168.161.24',
    port=22,
    username='root',
    pkey=private,
)

stdin, stdout, stderr = client.exec_command(command='cat /etc/shadow', timeout=1)
print(stdout.read().decode('utf-8'))

client.close()
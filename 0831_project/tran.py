#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/31
# usage: anlaysis logging


import paramiko



class Tran():
    def __init__(self, hostname, path, port, username ):
        self.hostname = hostname
        self.path = path
        self.port = port
        self.username = username
    @classmethod
    def createTran(cls, hostname, path):
        return cls(hostname=hostname, path=path, port=22, username='root')

    def putfile(self, shellname, shellpath='/mnt/monitor.sh'):
        '''
        put your shell scripts to web servers
        :param shellname:
        :return:
        '''
        private = paramiko.RSAKey.from_private_key_file(self.path)
        transport = paramiko.Transport((self.hostname, self.port))
        transport.connect(username=self.username, pkey=private)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(shellname, shellpath)
        transport.close()
    def getfile(self, logfile, webbool):
        '''
        get the reuslt log of web servers
        :param logfile:
        :param webbool:
        :return:
        '''
        private = paramiko.RSAKey.from_private_key_file(self.path)
        transport = paramiko.Transport((self.hostname, self.port))
        transport.connect(username=self.username, pkey=private)
        sftp = paramiko.SFTPClient.from_transport(transport)
        if webbool:
            sftp.get(logfile, '/mnt/web{}'.format(str(self.hostname) + '.log'))
        else:
            sftp.get(logfile, '/mnt/{}'.format(str(self.hostname) + '.log'))
        transport.close()
    def execommand(self, shellpath='/mnt/monitor.sh'):
        '''
        bash the shell scripts
        :param shellpath:
        :return:
        '''
        private = paramiko.RSAKey.from_private_key_file(self.path)
        transport = paramiko.Transport((self.hostname, self.port))
        transport.connect(username=self.username, pkey=private)
        client = paramiko.SSHClient()
        client._transport = transport
        _, _, stderr = client.exec_command('bash {}'.format(shellpath))
        print(stderr)
        client.close()

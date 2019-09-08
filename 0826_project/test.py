import paramiko

private = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
transport = paramiko.Transport(('192.168.161.24',22))
transport.connect(username='root', pkey=private)
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/mnt/0826_project/put_files/get_info.py','/mnt/0826_project/put_files/get_info.py')

sftp.close()
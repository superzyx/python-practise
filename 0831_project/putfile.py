#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date:2019/08/28
# usage: put files to serevrs


from lib.put_files import puts
from lib.connect_mysql import get_info

path = '/root/.ssh/id_rsa'
shell_path = '/root/getinfo.sh'
name = get_info.getinfo()
for hostname in name:
    puts.put_shell(hostname[0], path, shell_path)


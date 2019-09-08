#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date:2019/08/28
# usage: main of monitor


from lib.put_files.puts import exe_shell
from lib.connect_mysql.save_in import save,save_puv,save_top,save_status
from lib.connect_mysql.get_info import getinfo
from lib.get_logs.gets import get_logs,get_webinfo
from lib.analysis.call_ding import calling
from lib.analysis.puv_analysis import puv
from lib.analysis.top_ten import top
from lib.analysis.status_analysis import status
import time

path = '/root/.ssh/id_rsa'
log_path = '/mnt/server.log'
token = '2d42f1b28f99388f63482bda247d33fb3010a2576c9b6ff2b74e191752d1d509'
name = getinfo()
for hostname in name:
    print('请骚等')
    exe_shell(hostname[0], path)
    time.sleep(5)
    get_logs(hostname[0], path, log_path)
    get_webinfo(hostname[0], path)
    calling('/mnt/{}'.format(str(hostname[0])+'.log'), token)
    save('/mnt/{}'.format(str(hostname[0])+'.log'), hostname[0])
    pv, uv = puv()
    save_puv(pv, uv, hostname[0])
    save_top(top(), hostname[0])
    save_status(status(), hostname[0])

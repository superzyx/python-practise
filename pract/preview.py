#!/usr/bin/env python3
# ^3^ coding=utf8
#
# author: superzyx
# date: 2019/08/29
# usage: preview


# import requests
# import json
#
# out = requests.get(url='https://www.baidu.com', timeout=1)
# print(out.status_code)
# print(out.elapsed)
# print(out.url)
#
#
# api='https://oapi.dingtalk.com/robot/send?access_token=2d42f1b28f99388f63482bda247d33fb3010a2576c9b6ff2b74e191752d1d509'
# header = {'Content-Type': 'application/json'}
#
# data = {
#     "msgtype" : "text",
#     "text": {
#         "content": "测试发送测试信息至钉钉群"
#     },
#     'at': {
#         'atMobiles': [
#             '15180451886',
#         ]
#     },
#     'isAtAll': 'false'
# }
# senddata = json.dumps(data).encode('utf-8')
# requests.post(url=api, data=senddata, headers = header)

# import yagmail
#
# client = yagmail.SMTP(user='superzyx12138@163.com', password='superzyx12138', host='smtp.163.com')
# contents = ['林女士：','见信好！~ 服务器需要进行维护，请尽快处理']
# client.send(to=['2271958554@qq.com', 'superzyx12138@163.com'], subject='紧急邮件', contents=contents)



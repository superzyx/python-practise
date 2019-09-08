#!/usr/bin/env python3
# ^3^ coding= utf8
#
# author: superzyx
# date: 2019/08/16
# usage: practise try_expect_finally


# try:
#     print(1/0)
# except Exception as error:
#     print('[ERROR]:  {}'.format(error))
# finally:
#     pass
#
# print('adf')

#
# try:
#     a = input('请输入：')
#     if type(a) != int:
#         raise Exception('error')
# except Exception as error:
#     print('[ERROR] {}'.format(error))
# finally:
#     pass


tuple01 =(1, 2, 3, 4)
print(tuple01.index(4))
print(tuple01.count(tuple01[0]))
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo.py
   @author:zl
   @time:2022/04/08 17:13
   @software:PyCharm
   @desc:
"""
import ZL_mysqlCon_localhost as local

import requests,json

class Demo(object):

    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
    # def __init__(self):
    #     self.url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
    #     self.connect = sqlserver.connection
    #     self.cursor = sqlserver.cursor

    @classmethod
    def do_reptile(cls):
        while(True):
            print('请输入命令：')
            msg = input()
            if msg == 'exit':
                break
            response = requests.get(cls.url + msg)
            response.encoding = 'utf-8'
            resp = json.loads(response.text)
            print(resp.get('content'))

if __name__ == '__main__':
    sqlserver = local.LocalmySql()
    Demo.do_reptile()

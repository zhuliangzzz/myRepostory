#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:RbOASpider.py
   @author:zl
   @time:2022/06/24 11:25
   @software:PyCharm
   @desc:
"""
# 爬取oa消息
import json
import random
import sys

import fake_useragent
import requests
from ua_class.ua_info import UserAgent


class RbOASpider(object):
    def __init__(self):
        self.url = 'http://oa.redboard.com.cn:8082/CallSend/GetCallReceivePageList'
        self.Cookie = 'ASP.NET_SessionId=thwxcvf3jxgyeobn5403ltm2; UserAccount=802A20E427D29A35X407YKBAQ5U84OODXDTB; UserName=89BA84237BF34419X407YKBAQ5U84OODXDTB; __session:0.24807207126040187:=http:; __session:0.24807207126040187:menuids=300280'
        self.header = {'Cookie': self.Cookie, 'User-Agent': random.choice(UserAgent().chrome)}

    def get_msg(self, data):
        res = requests.post('http://oa.redboard.com.cn:8082/CallSend/GetCallReceivePageList', data=data,
                            headers=self.header).content.decode('utf-8')
        msglist = json.loads(res)
        msgdict = {}
        for msg in msglist:
            msgdict['username'] = msg.get('UserName')
            msgdict['content'] = msg.get('CallContent')
            msgdict['time'] = msg.get('CallTime')
            print(msgdict)
        # print(obj[0])
        # print(type(obj[0]))

    # 获取oa信息数量
    def getTotalCount(self):
        count = requests.get(url='http://oa.redboard.com.cn:8082/CallSend/GetCallReceiveCount',headers=self.header).text
        return count
        # return count

    # 自动登录
    def auto_login(self):
        pass

if __name__ == '__main__':
    oa_spider = RbOASpider()
    count = int(oa_spider.getTotalCount())
    print(count)
    for index in range(0,count//30 + 1):
        data = {
            'PageIndex': index,
            'pageSize': 30
        }
        oa_spider.get_msg(data)
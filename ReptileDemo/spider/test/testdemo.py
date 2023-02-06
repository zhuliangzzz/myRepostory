#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:testdemo.py
   @author:zl
   @time:2022/05/29 11:02
   @software:PyCharm
   @desc:
"""
# fake_useragent 随机生成一个浏览器用户代理
from urllib import parse, request

import fake_useragent

agent = fake_useragent.UserAgent()
header = {'User-Agent': agent.chrome}
url = 'https://www.baidu.com/s?wd='
s = input('input key word:')
word = parse.quote(s)
req = request.Request(url + word, headers=header)
res = request.urlopen(req)
html = res.read().decode('utf-8')
# 3.保存文件至当前目录
filename = word + '.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
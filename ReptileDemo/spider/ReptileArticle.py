#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:ReptileArticle.py
   @author:zl
   @time:2022/04/10 11:05
   @software:PyCharm
   @desc:
   爬取文章内容
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.bqkan8.com/1_1094/5403177.html'

if __name__ == '__main__':
    resp = requests.get(url)
    # print(resp.text)
    text = resp.text
    soup = BeautifulSoup(text, features='html.parser')
    content = soup.find_all('div', class_='showtxt')
    # print(content[0].text)
    print(content[0].text.replace('\xa0'*8, '\n\n'))

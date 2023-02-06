#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:MaoyanSpider.py
   @author:zl
   @time:2022/05/29 14:58
   @software:PyCharm
   @desc:
"""
import csv
import re
from urllib import request, parse
import fake_useragent


class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.header = fake_useragent.UserAgent().chrome

    def get_html(self, url):
        req = request.Request(url, headers={'User-Agent': self.header})
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        print(html)
        self.parseHtml(html)

    def parseHtml(self, html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        re_compile = re.compile(re_bds, re.S)
        re_list = re_compile.findall(html)
        self.saveHtml(re_list)

    def saveHtml(self, list):
        with open('maoyan.csv', 'a', newline='', encoding='utf-8') as r:
            writer = csv.writer(r)
        for l in list:
            name = l[0].strip()
            star = l[1].strip()[3:]
            time = l[2].strip()[5:]
            cont = [name, star, time]
            print(name, star, time)
            writer.writerow(cont)

    def run(self):
        for offset in range(0, 11, 10):
            self.get_html(self.url.format(offset))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()

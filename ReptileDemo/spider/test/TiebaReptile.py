#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:TiebaReptile.py
   @author:zl
   @time:2022/05/29 11:29
   @software:PyCharm
   @desc:
   爬取百度贴吧某数据
"""
import random
import time

import fake_useragent
from urllib import request, parse


class TiebaReptil(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'
        self.header = fake_useragent.UserAgent().chrome

    def get_html(self, url):
        req = request.Request(url, headers={'User-Agent': self.header})
        res = request.urlopen(req)
        # html = res.read().decode('utf-8', 'ignore')
        html = res.read().decode('gbk', 'ignore')
        return html

    def save_html(self, filename, html):
        with open(filename, 'w') as writer:
            writer.write(html)

    def run(self):
        name = input("请输入贴吧名称：")
        begin_page = int(input("起始页："))
        end_page = int(input("结束页："))
        for page in range(begin_page, end_page + 1):
            pn = (page - 1) * 50
            dataDic = {
                'kw': name,
                'pn': str(pn)
            }
            data = parse.urlencode(dataDic)
            html = self.get_html(self.url.format(data))
            filename = "%s-%s.html" % (name, page)
            self.save_html(filename, html)
            print("第%s页抓取成功！！！" % page)
            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    reptil = TiebaReptil()
    reptil.run()

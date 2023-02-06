#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:BaiduImageSpider.py
   @author:zl
   @time:2022/05/29 15:47
   @software:PyCharm
   @desc:
"""
import os
import re
from urllib import parse

import requests, fake_useragent


class BaiduImageSpider(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/flip?tn=baiduimage&word={}'
        self.header = {'User-Agent': fake_useragent.UserAgent().chrome}

    def get_image(self, url, word):
        res = requests.get(url, headers=self.header)
        res.encoding = 'utf-8'
        html = res.text
        pattern = re.compile('"hoverURL":"(.*?)"', re.S)
        findlist = pattern.findall(html)
        img_dir = './images/%s/' % word
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        i = 1
        print(findlist)
        for li in findlist:
            if not li:
                continue
            filename = "%s %s-%s.jpg" % (img_dir, word, i)
            self.save_image(li, filename)
            i += 1

    def save_image(self, img_link, filename):
        content = requests.get(img_link, headers=self.header).content
        with open(filename, 'wb') as w:
            w.write(content)
        print(filename, '下载完成')

    def run(self):
        word = input('请输入搜索的图片关键字：')
        url = self.url.format(parse.quote(word))
        self.get_image(url, word)


if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.run()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zl

import requests, os ,re

#爬取英雄头像
class HeroHeadPortrait:
    def __init__(self):
        #网址
        self.url = 'https://pvp.qq.com/web201605'
        self.header = {'User-Agent': ''}
        #图片保存路径
        self.imgSavePath = 'D://myfiles//files//hero//'

    def getHeadPortrait(self):
        response = requests.get(self.url+'/js/herolist.json')
        response.encoding = 'utf-8'
        herojson = response.json()
        #heroimages   game.gtimg.cn / images / yxzj / img201606 / skin / hero - info / 106 / 106 - bigskin - 6.jpg
        imageUrl = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info'
        for hero in herojson:
            #hero ename
            heroNo = hero['ename']
            heroName = hero['cname']

            os.makedirs(self.imgSavePath+heroName)
            # targetUrl = imageUrl + '/%s/%s-bigskin-%s.jpg' % (heroNo, heroNo, 1)
            # responseImg = requests.get(targetUrl)
            # if responseImg.status_code == 200:
            #     iv = re.split('-', targetUrl)
            #     open(iv[-1], 'wb').write(responseImg.content)
            for i in range(1, 12):
                targetUrl = imageUrl + '/%s/%s-bigskin-%s.jpg' % (heroNo, heroNo, i)
                responseImg = requests.get(targetUrl)
                if responseImg.status_code == 200:
                    iv = re.split('-', targetUrl)
                    open(self.imgSavePath+heroName+'/'+iv[-1], 'wb').write(responseImg.content)


if __name__ == '__main__':
    HeroHeadPortrait().getHeadPortrait()
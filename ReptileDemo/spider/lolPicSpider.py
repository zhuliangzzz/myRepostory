#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:lolPicSpider.py
   @author:zl
   @time:2022/07/20 15:55
   @software:PyCharm
   @desc:
   爬取lol壁纸
"""
import json
import os.path
import random
import time
from multiprocessing.pool import ThreadPool

import requests
from oaspider.ua_class.ua_info import UserAgent

headers = {'User-agent': random.choice(UserAgent().chrome)}


# 取到所有heroid
def getIdList():
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    res = requests.get(url, headers=headers).content.decode('utf-8')
    res_dict = json.loads(res)
    heros = res_dict.get('hero')
    idlist = []
    for hero in heros:
        idlist.append(hero.get('heroId'))
    return idlist


# 获取图片地址
def do_Reptile(url):
    data = requests.get(url, headers=headers).content.decode('utf-8')
    data_dict = json.loads(data)
    for i, skin in enumerate(data_dict['skins']):
        item = {}
        item['name'] = skin.get('heroName')
        item['skin_name'] = skin.get('name').replace('/', '_') if '/' in skin.get('name') else skin.get('name')
        if not skin.get('mainImg'):
            continue
        item['img_link'] = skin.get('mainImg')
        download(i + 1, item)


# download
def download(index, infodict):
    path = 'skins/' + infodict.get('name')
    if not os.path.exists(path):
        os.makedirs(path)
    content = requests.get(infodict.get('img_link'), headers=headers).content
    with open('./' + path + '/' + infodict.get('skin_name') + str(index) + '.jpg', 'wb') as w:
        w.write(content)


# 主方法
def Main():
    print(time.time())
    pool = ThreadPool(6)
    id_list = getIdList()
    pages = []
    for id in id_list:
        page = 'https://game.gtimg.cn/images/lol/act/img/js/hero/%s.js' % id
        pages.append(page)
    pool.map(do_Reptile, pages)
    pool.close()
    pool.join()
    print(time.time())


if __name__ == '__main__':
    Main()

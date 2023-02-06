#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zl
#爬取某网站上的数据信息

import requests
from bs4 import BeautifulSoup
from ZL_mysqlCon_localhost import LocalMySql


class Main:
    def __init__(self, keyword, page=1):
        self.sqlObj = LocalMySql()
        self.sqlCur = self.sqlObj.cursor
        self.keyword = keyword
        self.page = page

    def run_spider(self):
        url = "https://piao.qunar.com//ticket//list.htm?keyword=%s&region=&from=mpl_search_suggest&page=%s" % (self.keyword, self.page)
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        bsobj = BeautifulSoup(text, 'html.parser')
        arr = bsobj.find('div', {'class': 'result_list'}).contents
        for i in arr:
            info = i.attrs
            name = info.get('data-sight-name')
            addr = info.get('data-address')
            sale_count = info.get('data-sale-count')
            point = info.get('data-point')

            price = i.find('span', {'class': 'sight_item_price'})
            price = price.find_all('em')
            price = price[0].text
            print(price)

            print("景点名:", name, ",景点地址:", addr, ",月销量：", sale_count, ",经纬度：", point)
            sql = "insert into Sight_Info(name,address,count,point,price,city) values('%s','%s','%s','%s',%s,'%s')" % (
                name, addr, sale_count, point, price, self.keyword)
            try:
                self.sqlCur.execute(sql)
                self.sqlObj.connection.commit()
            except:
                self.sqlObj.connection.rollback()
        self.sqlObj.close_con()


if __name__ == '__main__':
    # citys = ['北京', '上海', '成都', '三亚', '广州', '重庆', '深圳', '西安', '杭州', '厦门', '武汉', '大连', '苏州']
    citys = ['海南', '江西']
    for city in citys:
        print(city)
        for i in range(1, 5):  #五页数据
                main = Main(city, page=i)
                main.run_spider()







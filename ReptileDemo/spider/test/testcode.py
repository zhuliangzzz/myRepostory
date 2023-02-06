#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:testcode.py
   @author:zl
   @time:2022/05/29 16:19
   @software:PyCharm
   @desc:
"""
import math

import  requests
import fake_useragent

# login_info = {
#     'UserAccount':'J53859',
#     'UserPassword':'Rb123456'
# }
login_info = ('J53859','Rb123456')

header = {'User-Agent': fake_useragent.UserAgent().chrome}
# get = requests.session().post('http://oa.redboard.com.cn:8082/Home/Index',data=login_info, headers=header)
# res = requests.get('http://oa.redboard.com.cn:8082/Home/Index', headers=header)
# print(res.text)

res = requests.get('http://oa.redboard.com.cn:8082/Home/Index', headers=header, auth=login_info)
print(res.content)




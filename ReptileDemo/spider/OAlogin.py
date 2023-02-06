#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:OAlogin.py
   @author:zl
   @time:2022/06/24 11:41
   @software:PyCharm
   @desc:
   实现oa账号密码登录
"""
import random
import sys

import requests
# import res_rc
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from test.ua_class.ua_info import UserAgent
import loginoa as ui


class OAlogin(object):
    def __init__(self):
        # 请求验证码
        self.loadYZM()
        self.login_url = 'http://oa.redboard.com.cn:8082/Account/Login'
        self.header = {'User-Agent': random.choice(UserAgent().chrome),'content-type':'application/x-www-form-urlencoded; charset=UTF-8','x-requested-with':'XMLHttpRequest'}
        regexp = QRegExp('\w+')
        validator = QRegExpValidator(regexp)
        window.username.setValidator(validator)
        window.password.setValidator(validator)
        window.login_btn.clicked.connect(self.login)
        window.reset_btn.clicked.connect(self.reset)

    def loadYZM(self):
        content = requests.get('http://oa.redboard.com.cn:8082/Account/Yzm',
                               headers={'User-Agent': random.choice(UserAgent().chrome)}).content
        with open('images/yzm.jpg','wb') as w:
            w.write(content)
        q_pixmap = QPixmap('images/yzm.jpg')
        window.yzmPic.setPixmap(q_pixmap)
        window.yzmPic.setScaledContents(True)

    def login(self):  # 登录操作
        username = window.username.text()
        password = window.password.text()
        yzm = window.yzm.text()
        if not username.strip():
            QMessageBox.warning(mainwidow, 'infomation', '用户名不能为空!', QMessageBox.Ok)
            return
        if not password.strip():
            QMessageBox.warning(mainwidow, 'infomation', '密码不能为空!', QMessageBox.Ok)
            return
        if not yzm.strip():
            QMessageBox.warning(mainwidow, 'infomation', '验证码不能为空!', QMessageBox.Ok)
            return
        params = {
            'UserAccount': username,
            'UserPassword': password,
            'YZM':yzm
        }
        self.login_oa(params)

    def login_oa(self, params):
        text = requests.post(self.login_url, data=params, headers=self.header,allow_redirects=False)
        print(text)

    def reset(self):  # 重置
        window.username.clear()
        window.password.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ui.Ui_MainWindow()
    mainwidow = QMainWindow()
    mainwidow.setWindowIcon(QIcon(':/icon/res/jasonzhang.jpg'))
    window.setupUi(mainwidow)
    o_alogin = OAlogin()
    mainwidow.show()
    sys.exit(app.exec_())
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:TranslatorProgram.py
   @author:zl
   @time:2022/06/20 16:39
   @software:PyCharm
   @desc:
"""
import hashlib
import random
import sys
import time

from PyQt5.QtGui import QIcon

import res_rc

import langid
import requests

# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit

import Translator as ui


class TranslatorProgram(object):
    def __init__(self):
        # form.currentText.keyPressEvent = self.newEvent
        form.currentText.textChanged.connect(self.translate)
        form.translate_btn.clicked.connect(self.translate)
        form.exit_btn.clicked.connect(lambda: sys.exit())

    def translate(self):
        # 翻译
        # 1.取到输入的翻译内容
        # 2.识别内容是何种语言
        # 3.调用api得到翻译后的内容并显示
        app.processEvents()
        content = form.currentText.toPlainText()
        if not content.strip():
            form.label.setText('自动检测语言')
            form.translatedText.clear()
            return
        classify = langid.classify(content)[0]
        if classify == 'zh':
            form.label.setText('中文  »  英语')
        elif classify == 'en':
            form.label.setText('英语  »  中文')
        elif classify == 'ko':
            form.label.setText('韩语  »  中文')
        elif classify == 'ja':
            form.label.setText('日语  »  中文')
        elif classify == 'it':
            form.label.setText('英文  »  中文')
        else:
            form.label.setText('暂时只能识别中文、英语、日语、韩语')
        content = form.currentText.toPlainText()
        spider = YouDaoSpider()
        translatedText = spider.translate(content)
        form.translatedText.setText('\n'.join(translatedText))

    # def newEvent(self, event):
    #     QTextEdit.keyPressEvent(form.currentText, event)
    #     if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
    #         self.translate()


# 有道翻译
class YouDaoSpider:
    def __init__(self):
        self.url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        # self.heaer = {'User-Agent': fake_useragent.UserAgent().firefox}
        # self.heaer = {'User-Agent': fake_useragent.UserAgent(path='ua.json').random}
        self.heaer = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

    def get_lts_salt_sign(self, word):
        lts = str(int(time.time() * 1000))
        salt = lts + str(random.randint(0, 9))
        string = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        md_ = hashlib.md5()
        md_.update(string.encode())
        sign = md_.hexdigest()
        return lts, salt, sign

    def attact_yd(self, word):
        lts, salt, sign = self.get_lts_salt_sign(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": "cda1e53e0c0eb8dd4002cefc117fa588",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        res = requests.post(url=self.url, data=data, headers=self.heaer)
        results = []
        for result in res.json().get('translateResult'):
            results.append(result[0].get('tgt'))
        return results

    def translate(self, word):
        res = self.attact_yd(word)
        return res


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setWindowIcon(QIcon(':/icon/res/jing.jpg'))
    widget = QWidget()
    form = ui.Ui_Form()
    form.setupUi(widget)
    program = TranslatorProgram()
    widget.show()
    sys.exit(app.exec_())

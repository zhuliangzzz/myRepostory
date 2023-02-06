# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\myfiles\pythonproject\ReptileDemo\spider\test\Translator.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(686, 353)
        Form.setStyleSheet("QWidget{background:#fff;}\n"
"QLabel { border:1px solid #aaa;    font: 10pt \"黑体\";\n"
"} QPushButton {padding-left:16px;padding-right:16px;border:none;border-radius:2px;} QPushButton#exit_btn{\n"
"color:#e02433;border:1px solid #e02433;}\n"
"QPushButton#translate_btn{\n"
"background:#e02433;color:white;\n"
"}QPushButton#exit_btn:hover{\n"
"background:#bf0917;color:white;border:1px solid #bf0917;cursor:PointingHandCursor;}\n"
" QPushButton#translate_btn:hover{\n"
"background:#bf0917;color:white;border:1px solid #bf0917;cursor:PointingHandCursor;}\n"
"QTextEdit{background:#f2f2f2;border-radius:4px;}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(30, 30, 30, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("padding:0 16px 0;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.translate_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translate_btn.sizePolicy().hasHeightForWidth())
        self.translate_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.translate_btn.setFont(font)
        self.translate_btn.setObjectName("translate_btn")
        self.horizontalLayout.addWidget(self.translate_btn)
        self.exit_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout.addWidget(self.exit_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.currentText = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.currentText.setFont(font)
        self.currentText.setObjectName("currentText")
        self.horizontalLayout_2.addWidget(self.currentText)
        self.translatedText = QtWidgets.QTextEdit(Form)
        self.translatedText.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.translatedText.setFont(font)
        self.translatedText.setReadOnly(True)
        self.translatedText.setObjectName("translatedText")
        self.horizontalLayout_2.addWidget(self.translatedText)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Translator Program"))
        self.label.setText(_translate("Form", "自动检测语言"))
        self.translate_btn.setText(_translate("Form", "翻译"))
        self.exit_btn.setText(_translate("Form", "退出"))
        self.currentText.setPlaceholderText(_translate("Form", "请输入你要翻译的文字"))


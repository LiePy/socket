# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
import time
import socket
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QObject
from test4.server_4 import BackendThread    # 导入自定义类


class Ui_Dialog(object):
    s = socket.socket()
    msg_send = ''
    msg_rec = ''
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(808, 320)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 753, 272))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_6.addWidget(self.textBrowser)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_6.addWidget(self.textBrowser_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "客户程序"))
        self.label.setText(_translate("Dialog", "服务器名称："))
        self.label_2.setText(_translate("Dialog", "服务器端口："))
        self.pushButton_4.setText(_translate("Dialog", "连接"))
        self.pushButton_5.setText(_translate("Dialog", "断开"))
        self.label_3.setText(_translate("Dialog", "消息："))
        self.pushButton_3.setText(_translate("Dialog", "发送"))
        self.label_4.setText(_translate("Dialog", "发送的消息"))
        self.label_5.setText(_translate("Dialog", "接受的消息"))
        self.lineEdit.setText("127.0.0.1")
        self.lineEdit_2.setText("21567")
        self.pushButton_3.clicked.connect(self.send_button)
        self.pushButton_4.clicked.connect(self.connect_button)
        self.pushButton_5.clicked.connect(self.break_button)

        # 调用自定义类，同server_4
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.thread = QThread()     # 创建进程
        self.backend.moveToThread(self.thread)
        self.thread.started.connect(self.backend.run)
        self.thread.start()

    def connect_button(self):       # 连接按钮
        add1 = self.lineEdit.text()
        add2 = self.lineEdit_2.text()
        self.s.connect((add1, int(add2)))
        print('已连接到服务器')
        t = threading.Thread(target=self.rec_msg)
        t.start()

    def break_button(self):     # 断开按钮
        self.s.close()
        print('已关闭服务器')

    def send_button(self):      # 发送按钮
        MSG = '[' + time.ctime() + ']:' +self.lineEdit_3.text() + '\n'
        self.s.send(MSG.encode('GB2312'))
        print('已发送:', MSG)
        self.msg_send += MSG
        self.textBrowser.setText(self.msg_send)
        self.lineEdit_3.setText('')

    def handleDisplay(self, data):      # 显示收到的消息
        self.textBrowser_2.setText(self.msg_rec)

    def rec_msg(self):      # 接受消息
        while 1:
            print('等待接受消息中。。。')
            msg = self.s.recv(1024).decode('GB2312')
            print('收到消息', msg)
            self.msg_rec += msg
            print(self.msg_rec)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 20:16
# @Author  : Lvp
# @File    : login.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QDialog
import sys
from main import MainWindow as MWindow
from mainwindow import Ui_MainWindow
from G_COMM.runXinguan import logger
from changePwd import Ui_Dialog
import sqlite3

import os

# 项目路径
# base_path = app_path().replace('\\', '/')
base_path = os.getcwd().replace('\\', '/')


class Ui_LoginWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect(f'{base_path}/sequence.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 252)
        MainWindow.setWindowIcon(QIcon(f'{base_path}/img/logo.png'))
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 71, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 72, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 250, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(0, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 100, 250, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(0, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 160, 262, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 设置输入框内容隐藏
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton.setDefault(True)
        self.pushButton.clicked.connect(self.get_user)
        self.pushButton_2.clicked.connect(self.change_pwd)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "高通量测序"))
        self.label.setText(_translate("MainWindow", "账号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))

    def get_user(self):
        login_user = self.lineEdit.text()
        login_pwd = self.lineEdit_2.text()
        logger.info(f'{login_user} 开始登录********')
        try:
            s_sql = """select pwd from users_ where userNm = ?"""
            result = self.cursor.execute(s_sql, (login_user,))
            pwd = result.fetchone()
            if pwd:
                if login_pwd == pwd[0]:
                    main.show()
                    login.close()
                else:
                    QMessageBox.warning(self.centralwidget, '警告', '用户名或密码错误', QMessageBox.Yes)
            else:
                QMessageBox.warning(self.centralwidget, '警告', '用户名不存在', QMessageBox.Yes)
        except Exception as e:
            logger.error(f'登录失败：{str(e)}')

    def change_pwd(self):
        login_user = self.lineEdit.text()
        login_pwd = self.lineEdit_2.text()
        try:
            s_sql = """select pwd from users_ where userNm = ?"""
            result = self.cursor.execute(s_sql, (login_user, ))
            pwd = result.fetchone()
            if pwd:
                if login_pwd == pwd[0]:
                    child_win.exec_()
                else:
                    QMessageBox.warning(self.centralwidget, '警告', '用户名或密码错误', QMessageBox.Yes)
            else:
                QMessageBox.warning(self.centralwidget, '警告', '用户名不存在', QMessageBox.Yes)
        except Exception as e:
            logger.error(f'登录失败：{str(e)}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    # 加载主界面
    main = MWindow()
    main_ui = Ui_MainWindow()
    main_ui.setupUi(main)

    # 修改密码界面
    child_win = QDialog()
    child_ui = Ui_Dialog()
    child_ui.setupUi(child_win)

    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

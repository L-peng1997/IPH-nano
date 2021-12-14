# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePwd.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import sys
import sqlite3
import os

# 项目路径
# base_path = app_path().replace('\\', '/')
base_path = os.getcwd().replace('\\', '/')


class Ui_Dialog(object):

    def __init__(self):
        self.conn = sqlite3.connect(f'{base_path}/sequence.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(504, 343)
        Dialog.setWindowIcon(QIcon(f'{base_path}/img/logo.png'))
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, QtCore.Qt.WindowContextHelpButtonHint)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 280, 262, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 30, 381, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.userEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.userEdit.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userEdit.setFont(font)
        self.userEdit.setObjectName("userEdit")
        self.horizontalLayout_2.addWidget(self.userEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pwdEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.pwdEdit.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pwdEdit.setFont(font)
        self.pwdEdit.setObjectName("pwdEdit")
        self.horizontalLayout_3.addWidget(self.pwdEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.newEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.newEdit.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newEdit.setFont(font)
        self.newEdit.setObjectName("newEdit")
        self.horizontalLayout_4.addWidget(self.newEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        self.pwdEdit.setEchoMode(QLineEdit.Password)
        self.newEdit.setEchoMode(QLineEdit.Password)
        self.pushButton.clicked.connect(self.update_pwd)
        self.pushButton_2.clicked.connect(self.delete_user)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "修改用户"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "删除"))
        self.label.setText(_translate("Dialog", "账号"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.label_3.setText(_translate("Dialog", "确认密码"))

    def update_pwd(self):
        new_user = str(self.userEdit.text())
        pwd1 = str(self.pwdEdit.text())
        pwd2 = str(self.newEdit.text())
        s_sql = """select * from users_ where userNm = ?"""
        result = self.cursor.execute(s_sql, (new_user, ))
        user_ = result.fetchone()
        if new_user and pwd1 and pwd2:
            if not user_:
                if pwd1 != pwd2:
                    QMessageBox.warning(self.layoutWidget, '警告', '两次密码输入不一致！', QMessageBox.Ok)
                else:
                    i_sql = """insert into users_(userNm, pwd) values (?,?)"""
                    self.cursor.execute(i_sql, (new_user, pwd1))
                    self.conn.commit()
                    QMessageBox.information(self.layoutWidget, '提示', '用户添加成功', QMessageBox.Yes)
                    self.userEdit.clear()
                    self.pwdEdit.clear()
                    self.newEdit.clear()
                    self.Dialog.close()
            else:
                if pwd1 != pwd2:
                    QMessageBox.warning(self.layoutWidget, '警告', '两次密码输入不一致！', QMessageBox.Ok)
                else:
                    u_sql = """update users_ set pwd=? where userNm=?"""
                    self.cursor.execute(u_sql, (pwd1, new_user))
                    self.conn.commit()
                    self.userEdit.clear()
                    self.pwdEdit.clear()
                    self.newEdit.clear()
                    QMessageBox.information(self.layoutWidget, '提示', '用户密码修改成功', QMessageBox.Yes)
                    self.Dialog.close()
        else:
            QMessageBox.warning(self.layoutWidget, '警告', '用户名或密码不能为空', QMessageBox.Ok)

    def delete_user(self):
        new_user = str(self.userEdit.text())
        pwd1 = str(self.pwdEdit.text())
        pwd2 = str(self.newEdit.text())
        s_sql = """select * from users_ where userNm = ?"""
        result = self.cursor.execute(s_sql, (new_user,))
        user_ = result.fetchone()
        if new_user and pwd1 and pwd2:
            if not user_:
                QMessageBox.information(self.layoutWidget, '提示', '用户不存在！', QMessageBox.Yes)
            else:
                if pwd1 != pwd2:
                    QMessageBox.warning(self.layoutWidget, '警告', '两次密码输入不一致！', QMessageBox.Ok)
                else:
                    d_sql = """delete from users_ where userNm=?"""
                    self.cursor.execute(d_sql, (new_user, ))
                    self.conn.commit()
                    self.userEdit.clear()
                    self.pwdEdit.clear()
                    self.newEdit.clear()
                    QMessageBox.information(self.layoutWidget, '提示', '用户删除成功！', QMessageBox.Yes)
                    self.Dialog.close()
        else:
            QMessageBox.warning(self.layoutWidget, '警告', '用户名或密码不能为空', QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

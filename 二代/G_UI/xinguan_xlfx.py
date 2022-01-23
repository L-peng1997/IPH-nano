# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xinguan_xlfx.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import re
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QRegExp
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QDialog
from PyQt5.QtGui import QRegExpValidator, QIntValidator
import os


class Ui_Dialog(QWidget):

    paramSignal = pyqtSignal(dict)
    startSignal = pyqtSignal(int)
    signal = 0

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(831, 344)

        # 设置标签字体
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        # 设置输入框字体
        font_le = QtGui.QFont()
        font_le.setPointSizeF(11)
        font_le.setBold(True)
        font_le.setWeight(75)

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(14, -10, 781, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # 序列文件
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xvlie_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xvlie_label.sizePolicy().hasHeightForWidth())
        self.xvlie_label.setSizePolicy(sizePolicy)
        self.xvlie_label.setMinimumSize(QtCore.QSize(100, 0))
        self.xvlie_label.setObjectName("xvlie_label")
        self.xvlie_label.setFont(font)
        self.horizontalLayout.addWidget(self.xvlie_label)
        self.xvlie_LE = QtWidgets.QLineEdit(self.widget)
        self.xvlie_LE.setObjectName("xvlie_LE")
        self.xvlie_LE.setFont(font_le)
        self.xvlie_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout.addWidget(self.xvlie_LE)
        self.xvlie_tbtn = QtWidgets.QToolButton(self.widget)
        self.xvlie_tbtn.setObjectName("xvlie_tbtn")
        self.xvlie_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.horizontalLayout.addWidget(self.xvlie_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        # 结果路径
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.result_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_label.sizePolicy().hasHeightForWidth())
        self.result_label.setSizePolicy(sizePolicy)
        self.result_label.setMinimumSize(QtCore.QSize(100, 0))
        self.result_label.setObjectName("result_label")
        self.result_label.setFont(font)
        self.horizontalLayout_2.addWidget(self.result_label)
        self.result_LE = QtWidgets.QLineEdit(self.widget)
        self.result_LE.setObjectName("result_LE")
        self.result_LE.setFont(font_le)
        self.result_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout_2.addWidget(self.result_LE)
        self.result_tbtn = QtWidgets.QToolButton(self.widget)
        self.result_tbtn.setObjectName("result_tbtn")
        self.result_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.horizontalLayout_2.addWidget(self.result_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.run_btn = QtWidgets.QPushButton(self.widget)
        self.run_btn.setMaximumSize(QtCore.QSize(100, 40))
        self.run_btn.setObjectName("run_btn")
        self.run_btn.setStyleSheet("QPushButton{\n"
                                   "    background:#2AC28F;\n"
                                   "    color:white;\n"
                                   "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                   "}\n"
                                   "QPushButton:hover{                    \n"
                                   "    background:#99CC99;\n"
                                   "}\n")
        self.horizontalLayout_3.addWidget(self.run_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.widget)
        self.cancel_btn.setMaximumSize(QtCore.QSize(100, 40))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setStyleSheet("QPushButton{\n"
                                      "    background:rgb(241, 84, 84);\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#FF6666;\n"
                                      "}\n")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.result_tbtn.clicked.connect(lambda: self.choose_path(self.result_LE))
        self.xvlie_tbtn.clicked.connect(lambda: self.open_file(self.xvlie_LE))

        self.run_btn.clicked.connect(self.receive_param)
        self.run_btn.clicked.connect(self.send_start_sig)
        self.cancel_btn.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.xvlie_label.setText(_translate("Dialog", "序列文件："))
        self.xvlie_tbtn.setText(_translate("Dialog", "..."))
        self.result_label.setText(_translate("Dialog", "结果路径："))
        self.result_tbtn.setText(_translate("Dialog", "..."))
        self.run_btn.setText(_translate("Dialog", "运行"))
        self.cancel_btn.setText(_translate("Dialog", "取消"))

    def open_file(self, lineEdit):
        """
        选择具体的文件
        :param lineEdit: 将内容写入具体的文本框
        :return:
        """
        directory1 = QFileDialog.getOpenFileName(self.Dialog, "选取文件", "./")
        lineEdit.setText(directory1[0])

    def choose_path(self, lineEdit):
        """
        选择结果存放路径
        :param lineEdit: 将内容写入具体的文本框
        :return:
        """
        directory1 = QFileDialog.getExistingDirectory(self.Dialog, "选取文件夹", "./")
        lineEdit.setText(directory1)


    def receive_param(self):
        """
        接收子窗口中的所有参数，并发送给主窗口
        :return: 当前工作路径
        """
        # 序列文件
        xvlie_file = self.xvlie_LE.text()
        # 结果路径
        result_path = self.result_LE.text()

        if not xvlie_file or not result_path:
            QMessageBox.warning(self, '警告', '参数不能为空！', QMessageBox.Ok)
        else:
            self.signal = 1
            # 根据起文件夹名称作为任务名称
            result = re.findall(r'.*/(.*?)\..*', xvlie_file)
            task_nm = result[0] if result else str(int(time.time()*1000))
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 由于主页面需要显示（样品名称、barcode）参数，所以在子页面这两个参数必须存在
            parmas = {
                'task_type': task_type,
                'task_name': task_nm,
                'sample_list': '',
                'barcode_list': '',
                'result_path': result_path,
                'xvlie_file': xvlie_file,
            }
            # print(parmas)
            self.paramSignal.emit(parmas)
            self.Dialog.close()

    def send_start_sig(self):
        """
        发送启动信号给主界面，来调用命令运行程序
        :return:
        """
        # print(f'发送的信号为：{self.signal}')
        self.startSignal.emit(self.signal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主窗口
    main = QDialog()
    main_ui = Ui_Dialog()
    main_ui.setupUi(main)
    # 显示
    main.show()
    # QMessageBox.warning()
    sys.exit(app.exec_())

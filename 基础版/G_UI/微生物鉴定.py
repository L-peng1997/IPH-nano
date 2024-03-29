# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '微生物鉴定.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import qtawesome
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QRegExp
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QDialog
from PyQt5.QtGui import QIcon, QRegExpValidator
from configparser import ConfigParser
import os
import re
import pandas as pd
from datetime import date
import subprocess


base_path = os.getcwd().replace('\\', '/')
config = ConfigParser()
config.read(f'{base_path}/G_CONFIG/config.ini', encoding='utf-8')


class Ui_Dialog(object):

    paramSignal = pyqtSignal(dict)
    startSignal = pyqtSignal(int)
    signal = 0

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        # 接收页面所有参数
        self.data_list = []
        # 获取本地sample.fa文件中的所有序列名称
        self.xvlie_list = []

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(800, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)

        # 设置标签字体
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)

        # 设置输入框字体
        font_le = QtGui.QFont()
        font_le.setPointSizeF(11)
        font_le.setBold(True)
        font_le.setWeight(75)
        
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 50, 671, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.work_path = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_path.sizePolicy().hasHeightForWidth())
        self.work_path.setSizePolicy(sizePolicy)
        self.work_path.setMinimumSize(QtCore.QSize(80, 0))
        self.work_path.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.work_path.setObjectName("work_path")
        self.work_path.setFont(self.font)
        self.horizontalLayout.addWidget(self.work_path)
        self.work_path_LE = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_path_LE.sizePolicy().hasHeightForWidth())
        self.work_path_LE.setSizePolicy(sizePolicy)
        self.work_path_LE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.work_path_LE.setObjectName("work_path_LE")
        self.work_path_LE.setFont(font_le)
        self.horizontalLayout.addWidget(self.work_path_LE)
        self.work_path_btn = QtWidgets.QToolButton(self.layoutWidget)
        self.work_path_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.work_path_btn.setObjectName("work_path_btn")
        self.horizontalLayout.addWidget(self.work_path_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMaximumSize(QtCore.QSize(20, 30))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox)
        self.file_list = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_list.sizePolicy().hasHeightForWidth())
        self.file_list.setSizePolicy(sizePolicy)
        self.file_list.setMinimumSize(QtCore.QSize(80, 0))
        self.file_list.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.file_list.setObjectName("file_list")
        self.file_list.setFont(self.font)
        self.horizontalLayout_2.addWidget(self.file_list)
        self.file_list_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.file_list_LE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.file_list_LE.setObjectName("file_list_LE")
        self.file_list_LE.setFont(font_le)
        self.horizontalLayout_2.addWidget(self.file_list_LE)
        self.file_list_btn = QtWidgets.QToolButton(self.layoutWidget)
        self.file_list_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.file_list_btn.setObjectName("file_list_btn")
        self.horizontalLayout_2.addWidget(self.file_list_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.work_path.setEnabled(False)
        self.work_path_LE.setEnabled(False)
        self.work_path_btn.setEnabled(False)
        self.file_list.setEnabled(False)
        self.file_list_LE.setEnabled(False)
        self.file_list_btn.setEnabled(False)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.reads_one = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reads_one.sizePolicy().hasHeightForWidth())
        self.reads_one.setSizePolicy(sizePolicy)
        self.reads_one.setMinimumSize(QtCore.QSize(80, 0))
        self.reads_one.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.reads_one.setObjectName("reads_one")
        self.reads_one.setFont(self.font)
        self.horizontalLayout_3.addWidget(self.reads_one)
        self.reads_one_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.reads_one_LE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.reads_one_LE.setObjectName("reads_one_LE")
        self.reads_one_LE.setFont(font_le)
        self.horizontalLayout_3.addWidget(self.reads_one_LE)
        self.reads1_btn = QtWidgets.QToolButton(self.layoutWidget)
        self.reads1_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.reads1_btn.setObjectName("reads1_btn")
        self.horizontalLayout_3.addWidget(self.reads1_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.reads_tow = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reads_tow.sizePolicy().hasHeightForWidth())
        self.reads_tow.setSizePolicy(sizePolicy)
        self.reads_tow.setMinimumSize(QtCore.QSize(80, 0))
        self.reads_tow.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.reads_tow.setObjectName("reads_tow")
        self.reads_tow.setFont(self.font)
        self.horizontalLayout_4.addWidget(self.reads_tow)
        self.reads_two_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.reads_two_LE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.reads_two_LE.setObjectName("reads_two_LE")
        self.reads_two_LE.setFont(font_le)
        self.horizontalLayout_4.addWidget(self.reads_two_LE)
        self.reads2_btn = QtWidgets.QToolButton(self.layoutWidget)
        self.reads2_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.reads2_btn.setObjectName("reads2_btn")
        self.horizontalLayout_4.addWidget(self.reads2_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.result_path = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_path.sizePolicy().hasHeightForWidth())
        self.result_path.setSizePolicy(sizePolicy)
        self.result_path.setMinimumSize(QtCore.QSize(80, 0))
        self.result_path.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result_path.setObjectName("result_path")
        self.result_path.setFont(self.font)
        self.horizontalLayout_5.addWidget(self.result_path)
        self.result_path_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.result_path_LE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.result_path_LE.setObjectName("result_path_LE")
        self.result_path_LE.setFont(font_le)
        self.horizontalLayout_5.addWidget(self.result_path_LE)
        self.result_btn = QtWidgets.QToolButton(self.layoutWidget)
        self.result_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.result_btn.setObjectName("result_btn")
        self.horizontalLayout_5.addWidget(self.result_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.sample_name = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_name.sizePolicy().hasHeightForWidth())
        self.sample_name.setSizePolicy(sizePolicy)
        self.sample_name.setMinimumSize(QtCore.QSize(80, 0))
        self.sample_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sample_name.setObjectName("sample_name")
        self.sample_name.setFont(self.font)
        self.horizontalLayout_6.addWidget(self.sample_name)
        self.sample_name_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.sample_name_LE.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sample_name_LE.setObjectName("sample_name_LE")
        self.sample_name_LE.setFont(font_le)
        self.horizontalLayout_6.addWidget(self.sample_name_LE)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.data_type = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_type.sizePolicy().hasHeightForWidth())
        self.data_type.setSizePolicy(sizePolicy)
        self.data_type.setMinimumSize(QtCore.QSize(80, 0))
        self.data_type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.data_type.setObjectName("data_type")
        self.data_type.setFont(self.font)
        self.horizontalLayout_8.addWidget(self.data_type)
        self.single_btn = QtWidgets.QRadioButton(self.layoutWidget)
        self.single_btn.setObjectName("single_btn")
        self.single_btn.setFont(self.font)
        self.single_btn.setChecked(True)
        self.single_btn.setAutoRepeat(False)
        self.reads_two_LE.setEnabled(False)
        self.reads_tow.setEnabled(False)
        self.reads2_btn.setEnabled(False)
        self.horizontalLayout_8.addWidget(self.single_btn)
        self.double_btn = QtWidgets.QRadioButton(self.layoutWidget)
        self.double_btn.setObjectName("double_btn")
        self.double_btn.setFont(self.font)
        # self.double_btn.setChecked(True)
        self.horizontalLayout_8.addWidget(self.double_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.thread_num = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thread_num.sizePolicy().hasHeightForWidth())
        self.thread_num.setSizePolicy(sizePolicy)
        self.thread_num.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.thread_num.setFont(font)
        self.thread_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thread_num.setObjectName("thread_num")
        self.thread_num.setFont(self.font)
        self.horizontalLayout_7.addWidget(self.thread_num)
        self.thread_num_LE = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thread_num_LE.sizePolicy().hasHeightForWidth())
        self.thread_num_LE.setSizePolicy(sizePolicy)
        self.thread_num_LE.setMaximumSize(QtCore.QSize(100, 30))
        self.thread_num_LE.setObjectName("thread_num_LE")
        self.thread_num_LE.setFont(font_le)
        re = QRegExp("^[1-9][0-9]{1,8}$")  # 正则:只允许出现大于0的整数
        re_ = QRegExpValidator(re, self.thread_num_LE)  # 实例化正则验证器
        self.thread_num_LE.setValidator(re_)
        self.thread_num_LE.setText('10')
        self.horizontalLayout_7.addWidget(self.thread_num_LE)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(200, 450, 401, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.runBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.runBtn.setFixedSize(QtCore.QSize(100, 30))
        self.runBtn.setObjectName("runBtn")
        self.runBtn.setStyleSheet("QPushButton{\n"
                                   "    background:#2AC28F;\n"
                                   "    color:white;\n"
                                   "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                   "}\n"
                                   "QPushButton:hover{                    \n"
                                   "    background:#99CC99;\n"
                                   "}\n")
        self.horizontalLayout_9.addWidget(self.runBtn)
        self.cancleBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.cancleBtn.setFixedSize(QtCore.QSize(100, 30))
        self.cancleBtn.setObjectName("cancleBtn")
        self.cancleBtn.setStyleSheet("QPushButton{\n"
                                      "    background:rgb(241, 84, 84);\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#FF6666;\n"
                                      "}\n")
        self.horizontalLayout_9.addWidget(self.cancleBtn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.work_path_btn.clicked.connect(lambda: self.choose_path(self.work_path_LE))
        self.result_btn.clicked.connect(lambda: self.choose_path(self.result_path_LE))
        self.reads1_btn.clicked.connect(lambda: self.open_file(self.reads_one_LE))
        self.reads2_btn.clicked.connect(lambda: self.open_file(self.reads_two_LE))
        self.file_list_btn.clicked.connect(lambda: self.open_file(self.file_list_LE))
        self.double_btn.toggled.connect(lambda: self.change_trim(self.double_btn))
        self.checkBox.toggled.connect(lambda: self.change_le(self.checkBox))
        self.cancleBtn.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.work_path.setText(_translate("Dialog", "工作目录："))
        self.work_path_btn.setText(_translate("Dialog", "..."))
        self.file_list.setText(_translate("Dialog", "文件列表："))
        self.file_list_btn.setText(_translate("Dialog", "..."))
        self.reads_one.setText(_translate("Dialog", "Reads1："))
        self.reads1_btn.setText(_translate("Dialog", "..."))
        self.reads_tow.setText(_translate("Dialog", "Reads2："))
        self.reads2_btn.setText(_translate("Dialog", "..."))
        self.result_path.setText(_translate("Dialog", "结果目录："))
        self.result_btn.setText(_translate("Dialog", "..."))
        self.sample_name.setText(_translate("Dialog", "样品名称："))
        self.data_type.setText(_translate("Dialog", "数据类型："))
        self.single_btn.setText(_translate("Dialog", "单端"))
        self.double_btn.setText(_translate("Dialog", "双端"))
        self.thread_num.setText(_translate("Dialog", "线程数："))
        self.runBtn.setText(_translate("Dialog", "运行"))
        self.cancleBtn.setText(_translate("Dialog", "取消"))

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

    def change_trim(self, btn):
        """
        若选择双端，则read2可操作
        :param btn:
        :return:
        """
        # print(btn.isChecked())
        if btn.isChecked():
            # print(self.checkBox.isChecked(), '*'*20)
            if not self.checkBox.isChecked():
                self.reads_two_LE.setEnabled(True)
                self.reads_tow.setEnabled(True)
                self.reads2_btn.setEnabled(True)

        elif not btn.isChecked():
            self.reads_two_LE.setEnabled(False)
            self.reads_tow.setEnabled(False)
            self.reads2_btn.setEnabled(False)

    def change_le(self, btn):
        """
        不勾选则该行和工作目录灰色，不可操作；若勾选则该行和工作目录可操作，read1，read2，样品名称行不可操作
        :param btn:
        :return:
        """
        # print(btn.isChecked())
        if btn.isChecked():
            self.reads_two_LE.setEnabled(False)
            self.reads_tow.setEnabled(False)
            self.reads2_btn.setEnabled(False)

            self.reads_one_LE.setEnabled(False)
            self.reads_one.setEnabled(False)
            self.reads1_btn.setEnabled(False)

            self.sample_name.setEnabled(False)
            self.sample_name_LE.setEnabled(False)

            self.work_path.setEnabled(True)
            self.work_path_LE.setEnabled(True)
            self.work_path_btn.setEnabled(True)

            self.file_list.setEnabled(True)
            self.file_list_LE.setEnabled(True)
            self.file_list_btn.setEnabled(True)
        elif not btn.isChecked():
            self.work_path.setEnabled(False)
            self.work_path_LE.setEnabled(False)
            self.work_path_btn.setEnabled(False)

            self.file_list.setEnabled(False)
            self.file_list_LE.setEnabled(False)
            self.file_list_btn.setEnabled(False)

            self.reads_one_LE.setEnabled(True)
            self.reads_one.setEnabled(True)
            self.reads1_btn.setEnabled(True)

            self.sample_name.setEnabled(True)
            self.sample_name_LE.setEnabled(True)
            if self.double_btn.isChecked():
                self.reads_two_LE.setEnabled(True)
                self.reads_tow.setEnabled(True)
                self.reads2_btn.setEnabled(True)
            else:
                self.reads_two_LE.setEnabled(False)
                self.reads_tow.setEnabled(False)
                self.reads2_btn.setEnabled(False)


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


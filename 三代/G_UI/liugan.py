# -*- coding:utf-8 -*-
# @Time: 2021/7/5 17:13
# @Author: Lvp
# Form implementation generated from reading ui file 'czckxl.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
"""
流感页面输入各个必要的文件夹"""
import sys
import uuid

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QDialog
from functools import partial


class Ui_Dialog(QWidget):

    paramSignal = pyqtSignal(dict)
    startSignal = pyqtSignal(int)
    signal = 0

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(724, 429)

        # 设置标签字体
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        # 设置输入框字体
        font_le = QtGui.QFont()
        font_le.setBold(True)

        self.run_btn = QtWidgets.QPushButton(Dialog)
        self.run_btn.setGeometry(QtCore.QRect(180, 350, 93, 28))
        self.run_btn.setObjectName("run_btn")
        self.run_btn.setStyleSheet("QPushButton{\n"
                                        "    background:#2AC28F;\n"
                                        "    color:white;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#99CC99;\n"
                                        "}\n")

        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(410, 350, 93, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setStyleSheet("QPushButton{\n"
                                        "    background:rgb(241, 84, 84);\n"
                                        "    color:white;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#FF6666;\n"
                                        "}\n")

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 650, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # fastq文件条件
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # spacerItem = QtWidgets.QSpacerItem(54, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout.addItem(spacerItem)
        self.ori_label = QtWidgets.QLabel(self.widget)
        self.ori_label.setObjectName("ori_label")
        self.ori_label.setFont(font)
        self.horizontalLayout.addWidget(self.ori_label)
        self.ori_LE = QtWidgets.QLineEdit(self.widget)
        self.ori_LE.setObjectName("ori_LE")
        # self.ori_LE.setFixedSize(QtCore.QSize(380, 30))
        self.ori_LE.setMinimumHeight(30)
        self.ori_LE.setFont(font_le)
        # 设置输入框禁止输入
        self.ori_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.ori_LE)
        self.ori_tbtn = QtWidgets.QToolButton(self.widget)
        self.ori_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.ori_tbtn.setObjectName("ori_tbtn")
        self.horizontalLayout.addWidget(self.ori_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 结果文件路径选择
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sample_label = QtWidgets.QLabel(self.widget)
        self.sample_label.setObjectName("sample_label")
        self.sample_label.setFont(font)
        self.horizontalLayout_2.addWidget(self.sample_label)
        self.sample_LE = QtWidgets.QLineEdit(self.widget)
        self.sample_LE.setObjectName("sample_LE")
        # self.ori_LE.setFixedSize(QtCore.QSize(380, 30))
        self.sample_LE.setMinimumHeight(30)
        self.sample_LE.setFont(font_le)
        # 设置输入框禁止输入
        self.sample_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_2.addWidget(self.sample_LE)
        self.sample_tbtn = QtWidgets.QToolButton(self.widget)
        self.sample_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.sample_tbtn.setObjectName("sample_tbtn")
        self.horizontalLayout_2.addWidget(self.sample_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 结果文件名称
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.resfile_label = QtWidgets.QLabel(self.widget)
        self.resfile_label.setObjectName("resfile_label")
        self.resfile_label.setFont(font)
        self.horizontalLayout_3.addWidget(self.resfile_label)
        self.resfile_LE = QtWidgets.QLineEdit(self.widget)
        self.resfile_LE.setObjectName("resfile_LE")
        self.resfile_LE.setMinimumHeight(30)
        self.resfile_LE.setFont(font_le)
        # 设置输入框禁止输入
        self.resfile_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_3.addWidget(self.resfile_LE)
        self.resfile_tbtn = QtWidgets.QToolButton(self.widget)
        self.resfile_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.resfile_tbtn.setObjectName("resfile_tbtn")
        self.horizontalLayout_3.addWidget(self.resfile_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.run_btn.clicked.connect(self.receive_param)
        self.run_btn.clicked.connect(self.send_start_sig)
        self.cancel_btn.clicked.connect(Dialog.close)
        self.ori_tbtn.clicked.connect(partial(self.choose_path, self.ori_LE))
        self.sample_tbtn.clicked.connect(partial(self.open_file, self.sample_LE))
        self.resfile_tbtn.clicked.connect(partial(self.choose_path, self.resfile_LE))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.run_btn.setText(_translate("Dialog", "运行"))
        self.cancel_btn.setText(_translate("Dialog", "取消"))
        self.ori_label.setText(_translate("Dialog", "起始路径："))
        self.ori_tbtn.setText(_translate("Dialog", "..."))
        self.sample_label.setText(_translate("Dialog", "样品列表："))
        self.sample_tbtn.setText(_translate("Dialog", "..."))
        self.resfile_label.setText(_translate("Dialog", "结果路径："))
        self.resfile_tbtn.setText(_translate("Dialog", "..."))

    def open_file(self, lineEdit):
        """
        选择具体的文件
        :param lineEdit: 将内容写入具体的文本框
        :return:
        """
        directory1 = QFileDialog.getOpenFileName(self.Dialog, "选取文件夹", "./")
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
        # 起始路径
        ori_path = self.ori_LE.text()
        # 样品列表文件
        sample_file = self.sample_LE.text()
        # 结果路径
        res_path = self.resfile_LE.text()

        if not ori_path:
            QMessageBox.warning(self, "警告", "请输入具体的起始路径！", QMessageBox.Ok)
        elif not sample_file:
            QMessageBox.warning(self, "警告", "请选择具体的样品文件！", QMessageBox.Ok)
        elif not res_path:
            QMessageBox.warning(self, "警告", "请选择指定的结果文件存放路径！", QMessageBox.Ok)
        else:
            self.signal = 1
            # 根据起始文件夹名称作为任务名称
            task_nm = str(uuid.uuid4())
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 由于主页面需要显示（样品名称、barcode）参数，所以在子页面这两个参数必须存在
            parmas = {
                'task_type': task_type,
                'task_name': task_nm,
                'sample_list': '',
                'barcode_list': '',
                'result_path': res_path,
                'ori_path': ori_path,
                'sample_file': sample_file,
            }
            # print(parmas)
            self.paramSignal.emit(parmas)
            self.Dialog.close()

    def send_start_sig(self):
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










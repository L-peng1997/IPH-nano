# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xinguan_xlpj.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QRegExp
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QDialog
from PyQt5.QtGui import QRegExpValidator, QIntValidator
import os
from configparser import ConfigParser

exepath = os.getcwd().replace('\\', '/')
config = ConfigParser()
# config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')
config.read('D:/工作项目/IPH-nano/三代/G_CONFIG/config.ini', encoding='utf-8')


class Ui_Dialog(QWidget):

    paramSignal = pyqtSignal(dict)
    startSignal = pyqtSignal(int)
    signal = 0

    def __init__(self, model_list):
        super(Ui_Dialog, self).__init__()
        self.model_list = model_list

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(831, 606)

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
        self.widget.setGeometry(QtCore.QRect(10, 55, 791, 441))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # 起始路径
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ori_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ori_label.sizePolicy().hasHeightForWidth())
        self.ori_label.setSizePolicy(sizePolicy)
        self.ori_label.setMinimumSize(QtCore.QSize(130, 0))
        self.ori_label.setObjectName("ori_label")
        self.ori_label.setFont(font)
        self.horizontalLayout.addWidget(self.ori_label)
        self.ori_LE = QtWidgets.QLineEdit(self.widget)
        self.ori_LE.setObjectName("ori_LE")
        self.ori_LE.setFont(font_le)
        self.ori_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout.addWidget(self.ori_LE)
        self.ori_tbtn = QtWidgets.QToolButton(self.widget)
        self.ori_tbtn.setObjectName("ori_tbtn")
        self.ori_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.horizontalLayout.addWidget(self.ori_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        # 列表文件
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_label.sizePolicy().hasHeightForWidth())
        self.list_label.setSizePolicy(sizePolicy)
        self.list_label.setMinimumSize(QtCore.QSize(130, 0))
        self.list_label.setObjectName("list_label")
        self.list_label.setFont(font)
        self.horizontalLayout_2.addWidget(self.list_label)
        self.list_LE = QtWidgets.QLineEdit(self.widget)
        self.list_LE.setObjectName("list_LE")
        self.list_LE.setFont(font_le)
        self.list_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout_2.addWidget(self.list_LE)
        self.list_tbtn = QtWidgets.QToolButton(self.widget)
        self.list_tbtn.setObjectName("list_tbtn")
        self.list_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.horizontalLayout_2.addWidget(self.list_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        # 结果路径
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.result_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_label.sizePolicy().hasHeightForWidth())
        self.result_label.setSizePolicy(sizePolicy)
        self.result_label.setMinimumSize(QtCore.QSize(130, 0))
        self.result_label.setObjectName("result_label")
        self.result_label.setFont(font)
        self.horizontalLayout_3.addWidget(self.result_label)
        self.result_LE = QtWidgets.QLineEdit(self.widget)
        self.result_LE.setObjectName("result_LE")
        self.result_LE.setFont(font_le)
        self.result_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout_3.addWidget(self.result_LE)
        self.result_tbtn = QtWidgets.QToolButton(self.widget)
        self.result_tbtn.setObjectName("result_tbtn")
        self.result_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.horizontalLayout_3.addWidget(self.result_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        # 模型文件
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.model_lb = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_lb.sizePolicy().hasHeightForWidth())
        self.model_lb.setSizePolicy(sizePolicy)
        self.model_lb.setMinimumSize(QtCore.QSize(130, 0))
        self.model_lb.setObjectName("model_lb")
        self.model_lb.setFont(font)
        self.horizontalLayout_4.addWidget(self.model_lb)
        self.model_box = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_box.sizePolicy().hasHeightForWidth())
        self.model_box.setSizePolicy(sizePolicy)
        self.model_box.setObjectName("model_box")
        self.model_box.setFont(font_le)
        self.model_box.addItems(self.model_list)
        self.model_box.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout_4.addWidget(self.model_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        # Primmer Schemes
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.schemes_LB = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schemes_LB.sizePolicy().hasHeightForWidth())
        self.schemes_LB.setSizePolicy(sizePolicy)
        self.schemes_LB.setMinimumSize(QtCore.QSize(130, 0))
        self.schemes_LB.setObjectName("schemes_LB")
        self.schemes_LB.setFont(font)
        self.horizontalLayout_5.addWidget(self.schemes_LB)
        self.schemes_LE = QtWidgets.QLineEdit(self.widget)
        self.schemes_LE.setObjectName("schemes_LE")
        self.schemes_LE.setFont(font_le)
        self.schemes_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.schemes_LE.setText('/home/admin1/IPH-nano/artic-ncov2019/primer_schemes')
        self.horizontalLayout_5.addWidget(self.schemes_LE)
        self.schemes_tbtn = QtWidgets.QToolButton(self.widget)
        self.schemes_tbtn.setObjectName("schemes_tbtn")
        self.schemes_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.horizontalLayout_5.addWidget(self.schemes_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        # Primmer Detail
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.detail_LB = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detail_LB.sizePolicy().hasHeightForWidth())
        self.detail_LB.setSizePolicy(sizePolicy)
        self.detail_LB.setMinimumSize(QtCore.QSize(130, 0))
        self.detail_LB.setObjectName("detail_LB")
        self.detail_LB.setFont(font)
        self.horizontalLayout_6.addWidget(self.detail_LB)
        self.detail_LE = QtWidgets.QLineEdit(self.widget)
        self.detail_LE.setText("nCoV-2019/V3")
        self.detail_LE.setObjectName("detail_LE")
        self.detail_LE.setFont(font_le)
        self.detail_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout_6.addWidget(self.detail_LE)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        # Max Length Filt
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.max_LB = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_LB.sizePolicy().hasHeightForWidth())
        self.max_LB.setSizePolicy(sizePolicy)
        self.max_LB.setMinimumSize(QtCore.QSize(130, 0))
        self.max_LB.setObjectName("max_LB")
        self.max_LB.setFont(font)
        self.horizontalLayout_7.addWidget(self.max_LB)
        self.max_LE = QtWidgets.QLineEdit(self.widget)
        self.max_LE.setText("700")
        self.max_LE.setObjectName("max_LE")
        self.max_LE.setFont(font_le)
        self.max_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout_7.addWidget(self.max_LE)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        # Min Length Filt
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.min_LB = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_LB.sizePolicy().hasHeightForWidth())
        self.min_LB.setSizePolicy(sizePolicy)
        self.min_LB.setMinimumSize(QtCore.QSize(130, 0))
        self.min_LB.setObjectName("min_LB")
        self.min_LB.setFont(font)
        self.horizontalLayout_8.addWidget(self.min_LB)
        self.min_LE = QtWidgets.QLineEdit(self.widget)
        self.min_LE.setText("400")
        self.min_LE.setObjectName("min_LE")
        self.min_LE.setFont(font_le)
        self.min_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalLayout_8.addWidget(self.min_LE)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(480, 520, 93, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setStyleSheet("QPushButton{\n"
                                      "    background:rgb(241, 84, 84);\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#FF6666;\n"
                                      "}\n")
        self.run_btn = QtWidgets.QPushButton(Dialog)
        self.run_btn.setGeometry(QtCore.QRect(200, 520, 93, 28))
        # self.run_btn = QtWidgets.QPushButton(self.layoutWidget)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.ori_tbtn.clicked.connect(lambda: self.choose_path(self.ori_LE))
        self.list_tbtn.clicked.connect(lambda: self.open_file(self.list_LE))
        self.result_tbtn.clicked.connect(lambda: self.choose_path(self.result_LE))

        self.run_btn.clicked.connect(self.receive_param)
        self.run_btn.clicked.connect(self.send_start_sig)
        self.cancel_btn.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ori_label.setText(_translate("Dialog", "       起始路径："))
        self.ori_tbtn.setText(_translate("Dialog", "..."))
        self.list_label.setText(_translate("Dialog", "       列表文件："))
        self.list_tbtn.setText(_translate("Dialog", "..."))
        self.result_label.setText(_translate("Dialog", "       结果路径："))
        self.result_tbtn.setText(_translate("Dialog", "..."))
        self.model_lb.setText(_translate("Dialog", "       纠错模型："))
        self.schemes_LB.setText(_translate("Dialog", "Primmer Schemes："))
        self.schemes_tbtn.setText(_translate("Dialog", "..."))
        self.detail_LB.setText(_translate("Dialog", " Primmer Detail："))
        self.max_LB.setText(_translate("Dialog", "Max Length Filt： "))
        self.min_LB.setText(_translate("Dialog", "Min Length Filt："))
        self.cancel_btn.setText(_translate("Dialog", "取消"))
        self.run_btn.setText(_translate("Dialog", "运行"))

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
        # 起始文件
        ori_path = self.ori_LE.text()
        # 列表文件
        list_path = self.list_LE.text()
        # 结果路径
        result_path = self.result_LE.text()
        # 模型名称
        model_name = self.comboBox.currentText()
        # Primmer Schemes
        schemes = self.schemes_LE.text()
        # Primmer Detail
        detail = self.detail_LE.text()
        # Max Length Filt
        max_length = self.max_LE.text()
        # Min Length Filt
        min_length = self.min_LE.text()

        if not ori_path or not list_path or not schemes or not result_path or not model_name \
                or not detail or not max_length or not min_length:
            QMessageBox.warning(self, '警告', '参数不能为空！', QMessageBox.Ok)
        else:
            self.signal = 1
            # 根据起文件夹名称作为任务名称
            task_nm = ori_path.split('/')[-1] if '/' in ori_path else ori_path
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 由于主页面需要显示（样品名称、barcode）参数，所以在子页面这两个参数必须存在
            parmas = {
                'task_type': task_type,
                'task_name': task_nm,
                'sample_list': '',
                'barcode_list': '',
                'result_path': result_path,

                'ori_path': ori_path,
                'list_path': list_path,
                'model_name': model_name,
                'schemes': schemes,
                'detail': detail,
                'max_length': max_length,
                'min_length': min_length,
            }
            print(parmas)
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

    con_model = config.get('Metagenome', 'model_list')
    model_list = con_model.split(',')


    app = QApplication(sys.argv)
    # 实例化主窗口
    main = QDialog()
    main_ui = Ui_Dialog(model_list)
    main_ui.setupUi(main)
    # 显示
    main.show()
    # QMessageBox.warning()
    sys.exit(app.exec_())


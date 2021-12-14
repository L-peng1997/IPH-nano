# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '序列拼接（基于参考序列）.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import sys
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
        Dialog.setFixedSize(750, 420)
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

        # 样品列表
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 40, 651, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sample_LB = QtWidgets.QLabel(self.widget)
        self.sample_LB.setObjectName("sample_LB")
        self.sample_LB.setFont(font)
        self.horizontalLayout.addWidget(self.sample_LB)
        self.sample_LE = QtWidgets.QLineEdit(self.widget)
        self.sample_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.sample_LE.setObjectName("sample_LE")
        self.sample_LE.setFont(font_le)
        self.sample_LE.setToolTip('输入样品列表文件路径，或手动输入样品名称通过空格隔开')
        self.horizontalLayout.addWidget(self.sample_LE)
        self.sample_TB = QtWidgets.QToolButton(self.widget)
        self.sample_TB.setMaximumSize(QtCore.QSize(30, 28))
        self.sample_TB.setObjectName("sample_TB")
        self.horizontalLayout.addWidget(self.sample_TB)
        # 起始路径
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(60, 90, 651, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_LB = QtWidgets.QLabel(self.widget1)
        self.start_LB.setObjectName("start_LB")
        self.start_LB.setFont(font)
        self.horizontalLayout_2.addWidget(self.start_LB)
        self.start_LE = QtWidgets.QLineEdit(self.widget1)
        self.start_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.start_LE.setObjectName("start_LE")
        self.start_LE.setFont(font_le)
        self.start_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start_LE.setToolTip('该路径下应含有1.cutadapt文件夹，其中的文件应以samplename.fp_1.fq.gz方式命名')
        self.horizontalLayout_2.addWidget(self.start_LE)
        self.start_TB = QtWidgets.QToolButton(self.widget1)
        self.start_TB.setMaximumSize(QtCore.QSize(30, 28))
        self.start_TB.setObjectName("start_TB")
        self.horizontalLayout_2.addWidget(self.start_TB)
        # 参考序列
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(60, 140, 651, 30))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.xvle_LB = QtWidgets.QLabel(self.widget2)
        self.xvle_LB.setObjectName("xvle_LB")
        self.xvle_LB.setFont(font)
        self.horizontalLayout_3.addWidget(self.xvle_LB)
        self.xvlie_LE = QtWidgets.QLineEdit(self.widget2)
        self.xvlie_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.xvlie_LE.setObjectName("xvlie_LE")
        self.xvlie_LE.setFont(font_le)
        self.xvlie_LE.setToolTip('含有一条序列的fasta文件')
        self.xvlie_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_3.addWidget(self.xvlie_LE)
        self.xvlie_TB = QtWidgets.QToolButton(self.widget2)
        self.xvlie_TB.setMaximumSize(QtCore.QSize(30, 28))
        self.xvlie_TB.setObjectName("xvlie_TB")
        self.horizontalLayout_3.addWidget(self.xvlie_TB)
        # 线程数
        self.widget3 = QtWidgets.QWidget(Dialog)
        self.widget3.setGeometry(QtCore.QRect(20, 230, 240, 30))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.thread_LB = QtWidgets.QLabel(self.widget3)
        self.thread_LB.setObjectName("thread_LB")
        self.thread_LB.setFont(font)
        self.horizontalLayout_4.addWidget(self.thread_LB)
        self.thread_LE = QtWidgets.QLineEdit(self.widget3)
        self.thread_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.thread_LE.setObjectName("thread_LE")
        self.thread_LE.setFont(font_le)
        re = QRegExp("^[1-9][0-9]{1,8}$")  # 正则:只允许出现大于0的整数
        re_ = QRegExpValidator(re, self)  # 实例化正则验证器
        self.thread_LE.setValidator(re_)
        self.thread_LE.setText('10')
        self.horizontalLayout_4.addWidget(self.thread_LE)
        # 测序深度
        self.widget4 = QtWidgets.QWidget(Dialog)
        self.widget4.setGeometry(QtCore.QRect(33, 280, 227, 30))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.depth_LB = QtWidgets.QLabel(self.widget4)
        self.depth_LB.setObjectName("depth_LB")
        self.depth_LB.setFont(font)
        self.horizontalLayout_5.addWidget(self.depth_LB)
        self.depth_LE = QtWidgets.QLineEdit(self.widget4)
        self.depth_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.depth_LE.setObjectName("depth_LE")
        self.depth_LE.setFont(font_le)
        self.depth_LE.setValidator(re_)
        self.depth_LE.setToolTip('测序深度小于该数值的位点会被N代替')
        self.depth_LE.setText('10')
        self.horizontalLayout_5.addWidget(self.depth_LE)
        # 测序质量
        self.widget5 = QtWidgets.QWidget(Dialog)
        self.widget5.setGeometry(QtCore.QRect(361, 280, 219, 30))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.quality_LB = QtWidgets.QLabel(self.widget5)
        self.quality_LB.setObjectName("quality_LB")
        self.quality_LB.setFont(font)
        self.horizontalLayout_6.addWidget(self.quality_LB)
        self.quality_LE = QtWidgets.QLineEdit(self.widget5)
        self.quality_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.quality_LE.setObjectName("quality_LE")
        self.quality_LE.setFont(font_le)
        self.quality_LE.setValidator(QIntValidator(0, 40))
        self.quality_LE.setMaxLength(2)
        self.quality_LE.setToolTip('小于该数值的碱基会被废弃')
        self.quality_LE.setText('20')
        self.horizontalLayout_6.addWidget(self.quality_LE)
        # snp
        self.widget6 = QtWidgets.QWidget(Dialog)
        self.widget6.setGeometry(QtCore.QRect(372, 230, 210, 30))
        self.widget6.setObjectName("widget6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        # spacerItem1 = QtWidgets.QSpacerItem(52, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_7.addItem(spacerItem1)
        # 2021-08-16 14:27:37 添加snp勾选框
        # self.snp_check = QtWidgets.QCheckBox(self.widget6)
        # self.snp_check.setText("")
        # self.snp_check.setObjectName("snp_check")
        # self.snp_check.setChecked(True)
        # self.horizontalLayout_7.addWidget(self.snp_check)
        self.snp_LB = QtWidgets.QLabel(self.widget6)
        self.snp_LB.setObjectName("snp_LB")
        self.snp_LB.setFont(font)
        self.horizontalLayout_7.addWidget(self.snp_LB)
        self.snp_LE = QtWidgets.QLineEdit(self.widget6)
        self.snp_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.snp_LE.setObjectName("snp_LE")
        self.snp_LE.setFont(font_le)
        re = QRegExp("1|(0[\.][0-9]*)")  # 正则:只允许出现的数字
        re_validato = QRegExpValidator(re, self)  # 实例化正则验证器
        self.snp_LE.setValidator(re_validato)
        self.snp_LE.setToolTip('碱基比例高于该数值的位点会被列入SNP位点列表中')
        self.snp_LE.setText('0.1')
        self.horizontalLayout_7.addWidget(self.snp_LE)
        # 测序类型
        self.widget7 = QtWidgets.QWidget(Dialog)
        self.widget7.setGeometry(QtCore.QRect(60, 190, 400, 22))
        self.widget7.setObjectName("widget7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.type_LB = QtWidgets.QLabel(self.widget7)
        self.type_LB.setObjectName("type_LB")
        self.type_LB.setFont(font)
        self.horizontalLayout_8.addWidget(self.type_LB)
        self.single_RB = QtWidgets.QRadioButton(self.widget7)
        self.single_RB.setObjectName("single_RB")
        self.single_RB.setFont(font)
        self.single_RB.setChecked(True)
        self.horizontalLayout_8.addWidget(self.single_RB)
        self.double_RB = QtWidgets.QRadioButton(self.widget7)
        self.double_RB.setObjectName("double_RB")
        self.double_RB.setFont(font)
        self.horizontalLayout_8.addWidget(self.double_RB)
        # 运行、取消按钮
        self.run_btn = QtWidgets.QPushButton(Dialog)
        self.run_btn.setGeometry(QtCore.QRect(180, 360, 93, 28))
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
        self.cancel_btn.setGeometry(QtCore.QRect(400, 360, 93, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setStyleSheet("QPushButton{\n"
                                      "    background:rgb(241, 84, 84);\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#FF6666;\n"
                                      "}\n")
        #
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.start_TB.clicked.connect(lambda: self.choose_path(self.start_LE))
        self.sample_TB.clicked.connect(lambda: self.open_file(self.sample_LE))
        self.xvlie_TB.clicked.connect(lambda: self.open_file(self.xvlie_LE))
        # 2021-08-16 14:33:08 snp勾选框绑定事件
        # self.snp_check.toggled.connect(lambda: self.change_trim(self.snp_check))
        self.run_btn.clicked.connect(self.receive_param)
        self.run_btn.clicked.connect(self.send_start_sig)
        self.cancel_btn.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sample_LB.setText(_translate("Dialog", "样品列表"))
        self.sample_TB.setText(_translate("Dialog", "..."))
        self.start_LB.setText(_translate("Dialog", "起始路径"))
        self.start_TB.setText(_translate("Dialog", "..."))
        self.xvle_LB.setText(_translate("Dialog", "参考序列"))
        self.xvlie_TB.setText(_translate("Dialog", "..."))
        self.thread_LB.setText(_translate("Dialog", "线程数"))
        self.depth_LB.setText(_translate("Dialog", "测序深度阈值"))
        self.quality_LB.setText(_translate("Dialog", "测序质量阈值"))
        self.snp_LB.setText(_translate("Dialog", "SNP阈值"))
        self.type_LB.setText(_translate("Dialog", "测序类型"))
        self.single_RB.setText(_translate("Dialog", "单端测序"))
        self.double_RB.setText(_translate("Dialog", "双端测序"))
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

    def change_trim(self, btn):
        """
        根据snp是否勾选来修改snp参数的可用性
        :param btn:
        :return:
        """
        # print(btn.isChecked())
        if btn.isChecked():
            self.snp_LE.setEnabled(True)
            self.snp_LB.setEnabled(True)
        elif not btn.isChecked():
            self.snp_LE.setEnabled(False)
            self.snp_LB.setEnabled(False)

    def deal_sample(self):
        """
        处理窗口传递的样品列表参数
        可能为文件或用户手动输入
        :return:
        """
        sample_text = self.sample_LE.text()
        if os.path.isfile(sample_text):
            with open(sample_text, 'r') as f:
                content = f.read().splitlines()
                sample_list = [i for i in content if i != '']
        else:
            result = sample_text.split(' ')
            sample_list = [i for i in result if i != '']

        return sample_list

    def receive_param(self):
        """
        接收子窗口中的所有参数，并发送给主窗口
        :return: 当前工作路径
        """
        # 样品列表文件
        sample_list = self.deal_sample()
        # 起始路径
        start_file = self.start_LE.text()
        # 参考序列
        xvlie_path = self.xvlie_LE.text()
        # 测序类型
        cexv_type = ''
        if self.single_RB.isChecked():
            cexv_type = 'SE'
        elif self.double_RB.isChecked():
            cexv_type = 'PE'
        # 线程数
        threads_ = self.thread_LE.text()
        # SNP阈值
        snp = self.snp_LE.text()
        # 测序深度阈值
        depth = self.depth_LE.text()
        # 测序质量阈值
        quality = self.quality_LE.text()

        # 判断fastq文件中的第一个字符为'>'并且有且仅有一个
        if os.path.isfile(xvlie_path):
            try:
                with open(xvlie_path, 'r') as f:
                    file_content = f.read()
                # 文件的首个字符为'>'
                findex = file_content.index('>')
                # 文件中有且只有一个‘>’
                count = file_content.count('>')
            except Exception as e:
                print(f'文件读取失败：{e}')
                findex = 1
                count = 2
        else:
            findex = 1
            count = 2

        if not start_file or not sample_list or not threads_ or not depth or not quality:
            QMessageBox.warning(self, '警告', '参数不能为空！', QMessageBox.Ok)
        elif findex != 0 or count != 1:
            QMessageBox.warning(self, '警告', '参考序列文件格式存在错误', QMessageBox.Ok)
        else:
            self.signal = 1
            # 根据起文件夹名称作为任务名称
            task_nm = start_file.split('/')[-1] if '/' in start_file else start_file
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 由于主页面需要显示（样品名称、barcode）参数，所以在子页面这两个参数必须存在
            parmas = {
                'task_type': task_type,
                'task_name': task_nm,
                'sample_list': sample_list,
                'barcode_list': '',
                'work_file': start_file,
                'cexv_type': cexv_type,
                'xvlie_file': xvlie_path,
                'snp': snp,
                'threads': threads_,
                'depth': depth,
                'quality': quality,
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

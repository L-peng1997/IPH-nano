# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xlpj_erdai.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QRegExp
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QDialog
from PyQt5.QtGui import QRegExpValidator


class Ui_Dialog(QWidget):

    paramSignal = pyqtSignal(dict)
    startSignal = pyqtSignal(int)
    signal = 0

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(745, 450)

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


        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(52, 52, 620, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path_LB = QtWidgets.QLabel(self.widget)
        self.path_LB.setObjectName("path_LB")
        self.path_LB.setFont(font)
        self.horizontalLayout.addWidget(self.path_LB)
        self.path_LE = QtWidgets.QLineEdit(self.widget)
        self.path_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.path_LE.setObjectName("path_LE")
        self.path_LE.setFont(font_le)
        self.path_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.path_LE)
        self.path_btn = QtWidgets.QToolButton(self.widget)
        self.path_btn.setMaximumSize(QtCore.QSize(30, 28))
        self.path_btn.setObjectName("path_btn")
        self.horizontalLayout.addWidget(self.path_btn)

        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(52, 245, 550, 100))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cut_LB = QtWidgets.QLabel(self.widget1)
        self.cut_LB.setObjectName("cut_LB")
        self.cut_LB.setFont(font)
        self.horizontalLayout_6.addWidget(self.cut_LB)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.read1_LB = QtWidgets.QLabel(self.widget1)
        self.read1_LB.setObjectName("read1_LB")
        self.read1_LB.setFont(font)
        self.horizontalLayout_4.addWidget(self.read1_LB)
        self.read1_LB1 = QtWidgets.QLabel(self.widget1)
        self.read1_LB1.setObjectName("read1_LB1")
        self.read1_LB1.setFont(font_le)
        self.horizontalLayout_4.addWidget(self.read1_LB1)
        self.read1f_LE = QtWidgets.QLineEdit(self.widget1)
        self.read1f_LE.setMinimumSize(QtCore.QSize(20, 25))
        self.read1f_LE.setObjectName("read1f_LE")
        self.read1f_LE.setFont(font_le)
        self.read1f_LE.setText('10')
        self.horizontalLayout_4.addWidget(self.read1f_LE)
        self.read1_LB2 = QtWidgets.QLabel(self.widget1)
        self.read1_LB2.setObjectName("read1_LB2")
        self.read1_LB2.setFont(font_le)
        self.horizontalLayout_4.addWidget(self.read1_LB2)
        self.read1t_LE = QtWidgets.QLineEdit(self.widget1)
        self.read1t_LE.setMinimumSize(QtCore.QSize(20, 25))
        self.read1t_LE.setObjectName("read1t_LE")
        self.read1t_LE.setFont(font_le)
        self.read1t_LE.setText('3')
        self.horizontalLayout_4.addWidget(self.read1t_LE)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.read2_LB = QtWidgets.QLabel(self.widget1)
        self.read2_LB.setObjectName("read2_LB")
        self.read2_LB.setFont(font)
        self.horizontalLayout_5.addWidget(self.read2_LB)
        self.read2f_LB = QtWidgets.QLabel(self.widget1)
        self.read2f_LB.setObjectName("read2f_LB")
        self.read2f_LB.setFont(font_le)
        self.horizontalLayout_5.addWidget(self.read2f_LB)
        self.read2f_LE = QtWidgets.QLineEdit(self.widget1)
        self.read2f_LE.setMinimumSize(QtCore.QSize(20, 25))
        self.read2f_LE.setObjectName("read2f_LE")
        self.read2f_LE.setFont(font_le)
        self.read2f_LE.setText('10')
        self.horizontalLayout_5.addWidget(self.read2f_LE)
        self.read2t_LB = QtWidgets.QLabel(self.widget1)
        self.read2t_LB.setObjectName("read2t_LB")
        self.read2t_LB.setFont(font_le)
        self.horizontalLayout_5.addWidget(self.read2t_LB)
        self.read2t_LE = QtWidgets.QLineEdit(self.widget1)
        self.read2t_LE.setMinimumSize(QtCore.QSize(20, 25))
        self.read2t_LE.setObjectName("read2t_LE")
        self.read2t_LE.setFont(font_le)
        self.read2t_LE.setText('3')
        self.horizontalLayout_5.addWidget(self.read2t_LE)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.read2f_LE.setEnabled(False)
        self.read2t_LE.setEnabled(False)
        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.widget3 = QtWidgets.QWidget(Dialog)
        self.widget3.setGeometry(QtCore.QRect(66, 100, 605, 32))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sample_LB = QtWidgets.QLabel(self.widget3)
        self.sample_LB.setObjectName("sample_LB")
        self.sample_LB.setFont(font)
        self.horizontalLayout_8.addWidget(self.sample_LB)
        self.sample_LE = QtWidgets.QLineEdit(self.widget3)
        self.sample_LE.setMinimumSize(QtCore.QSize(0, 30))
        self.sample_LE.setObjectName("sample_LE")
        self.sample_LE.setFont(font_le)
        self.sample_LE.setToolTip('输入样品列表文件路径，或手动输入样品名称通过空格隔开')
        self.horizontalLayout_8.addWidget(self.sample_LE)
        self.sample_btn = QtWidgets.QToolButton(self.widget3)
        self.sample_btn.setMaximumSize(QtCore.QSize(30, 28))
        self.sample_btn.setObjectName("sample_btn")
        self.horizontalLayout_8.addWidget(self.sample_btn)

        self.widget4 = QtWidgets.QWidget(Dialog)
        self.widget4.setGeometry(QtCore.QRect(52, 210, 400, 22))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.type_LB = QtWidgets.QLabel(self.widget4)
        self.type_LB.setObjectName("type_LB")
        self.type_LB.setFont(font)
        self.horizontalLayout_3.addWidget(self.type_LB)
        self.single_radio = QtWidgets.QRadioButton(self.widget4)
        self.single_radio.setChecked(True)
        self.single_radio.setAutoRepeat(False)
        self.single_radio.setObjectName("single_radio")
        self.single_radio.setFont(font_le)
        self.horizontalLayout_3.addWidget(self.single_radio)
        self.double_radio = QtWidgets.QRadioButton(self.widget4)
        self.double_radio.setObjectName("double_radio")
        self.double_radio.setFont(font_le)
        self.horizontalLayout_3.addWidget(self.double_radio)

        self.widget5 = QtWidgets.QWidget(Dialog)
        self.widget5.setGeometry(QtCore.QRect(52, 155, 400, 22))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.platform_LB = QtWidgets.QLabel(self.widget5)
        self.platform_LB.setObjectName("platform_LB")
        self.platform_LB.setFont(font)
        self.horizontalLayout_2.addWidget(self.platform_LB)
        self.ill_radio = QtWidgets.QRadioButton(self.widget5)
        self.ill_radio.setChecked(True)
        self.ill_radio.setObjectName("ill_radio")
        self.ill_radio.setFont(font_le)
        self.horizontalLayout_2.addWidget(self.ill_radio)
        self.huada_radio = QtWidgets.QRadioButton(self.widget5)
        self.huada_radio.setObjectName("huada_radio")
        self.huada_radio.setFont(font_le)
        self.horizontalLayout_2.addWidget(self.huada_radio)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        re = QRegExp("^[0-9]*[1-9][0-9]*$")  # 正则:只允许出现的数字
        re_validato = QRegExpValidator(re, self)  # 实例化正则验证器
        self.read1f_LE.setValidator(re_validato)  # 设置验证
        self.read1t_LE.setValidator(re_validato)  # 设置验证
        self.read2f_LE.setValidator(re_validato)  # 设置验证
        self.read2t_LE.setValidator(re_validato)  # 设置验证

        self.double_radio.toggled.connect(lambda: self.change_trim(self.double_radio))
        self.path_btn.clicked.connect(lambda: self.choose_path(self.path_LE))
        self.sample_btn.clicked.connect(lambda: self.open_file(self.sample_LE))
        self.run_btn.clicked.connect(self.receive_param)
        self.run_btn.clicked.connect(self.send_start_sig)
        self.cancel_btn.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.run_btn.setText(_translate("Dialog", "运行"))
        self.cancel_btn.setText(_translate("Dialog", "取消"))
        self.path_LB.setText(_translate("Dialog", "    起始路径："))
        self.path_btn.setText(_translate("Dialog", "..."))
        self.cut_LB.setText(_translate("Dialog", "    序列修剪："))
        self.read1_LB.setText(_translate("Dialog", "read1:"))
        self.read1_LB1.setText(_translate("Dialog", "trim_front"))
        self.read1_LB2.setText(_translate("Dialog", "trim_tail"))
        self.read2_LB.setText(_translate("Dialog", "read2:"))
        self.read2f_LB.setText(_translate("Dialog", "trim_front"))
        self.read2t_LB.setText(_translate("Dialog", "trim_tail"))
        self.sample_LB.setText(_translate("Dialog", "样品列表："))
        self.sample_btn.setText(_translate("Dialog", "..."))
        self.type_LB.setText(_translate("Dialog", "    测序类型："))
        self.single_radio.setText(_translate("Dialog", "单端测序"))
        self.double_radio.setText(_translate("Dialog", "双端测序"))
        self.platform_LB.setText(_translate("Dialog", "    测序平台："))
        self.ill_radio.setText(_translate("Dialog", "Illumina"))
        self.huada_radio.setText(_translate("Dialog", "华大"))

    def change_trim(self, btn):
        """
        根据双端测序是否勾选来修改序列修剪第二行参数的可用性
        :param btn:
        :return:
        """
        if btn.isChecked():
            self.read2f_LE.setEnabled(True)
            self.read2t_LE.setEnabled(True)
        elif not btn.isChecked():
            self.read2f_LE.setEnabled(False)
            self.read2t_LE.setEnabled(False)

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
        # 起始文件夹路径
        start_file = self.path_LE.text()
        # 样品列表文件
        sample_list = self.deal_sample()
        # 其他参数
        platfrom = ''
        cexv_type = ''
        trim_front2 = ''
        trim_tail2 = ''
        trim_front1 = ''
        trim_tail1 = ''

        # 测序平台
        if self.ill_radio.isChecked():
            platfrom = 'illumina'
        elif self.huada_radio.isChecked():
            platfrom = 'huada'
        # 序列修剪参数
        if self.single_radio.isChecked():
            cexv_type = 'single'
            trim_front1 = self.read1f_LE.text()
            trim_tail1 = self.read1t_LE.text()
        elif self.double_radio.isChecked():
            cexv_type = 'double'
            trim_front1 = self.read1f_LE.text()
            trim_tail1 = self.read1t_LE.text()
            trim_front2 = self.read2f_LE.text()
            trim_tail2 = self.read2t_LE.text()
        if not start_file:
            QMessageBox.warning(self, "警告", "起始文件夹不存在！", QMessageBox.Ok)
        elif not sample_list:
            QMessageBox.warning(self, "警告", "样品列表不能为空或文件格式存在问题", QMessageBox.Ok)
        elif (self.single_radio.isChecked() and (not trim_tail1 or not trim_front1)) or (self.double_radio.isChecked()
            and (not trim_tail1 or not trim_front1 or not trim_tail2 or not trim_front2)):
            QMessageBox.warning(self, "警告", "请输入序列修剪相关参数", QMessageBox.Yes)
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
                'platform': platfrom,
                'cexv_type': cexv_type,
                'trim_front1': trim_front1,
                'trim_tail1': trim_tail1,
                'trim_front2': trim_front2,
                'trim_tail2': trim_tail2
            }
            # print(parmas)
            # 将子界面的所有参数传递给主界面
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


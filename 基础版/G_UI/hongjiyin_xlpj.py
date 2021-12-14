# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 15:57
# @Author  : Lvp
# @File    : hongjiyin_xlpj.py
"""
宏基因组-序列拼接条件页面输入各个必要的文件夹
"""
import sys
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
        Dialog.setFixedSize(787, 450)

        # 设置标签字体
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        # 设置输入框字体
        font_le = QtGui.QFont()
        font_le.setBold(True)

        # 运行按钮
        self.run_btn = QtWidgets.QPushButton(Dialog)
        self.run_btn.setGeometry(QtCore.QRect(190, 360, 100, 28))
        self.run_btn.setObjectName("run_btn")
        self.run_btn.setStyleSheet("QPushButton{\n"
                                        "    background:#2AC28F;\n"
                                        "    color:white;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#99CC99;\n"
                                        "}\n")
        # 取消按钮
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(480, 360, 100, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.setStyleSheet("QPushButton{\n"
                                        "    background:rgb(241, 84, 84);\n"
                                        "    color:white;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#FF6666;\n"
                                        "}\n")

        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 35, 720, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        # fastq文件
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.fastq_label = QtWidgets.QLabel(self.layoutWidget)
        self.fastq_label.setObjectName("fastq_label")
        self.fastq_label.setFont(font)
        self.horizontalLayout_5.addWidget(self.fastq_label)
        self.fastq_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.fastq_LE.setObjectName("fastq_LE")
        self.fastq_LE.setFont(font_le)
        self.fastq_LE.setMinimumHeight(30)
        self.fastq_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_5.addWidget(self.fastq_LE)
        self.fastq_tbtn = QtWidgets.QToolButton(self.layoutWidget)
        self.fastq_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.fastq_tbtn.setObjectName("fastq_tbtn")
        self.horizontalLayout_5.addWidget(self.fastq_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        # 结果文件路径
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.respath_label = QtWidgets.QLabel(self.layoutWidget)
        self.respath_label.setObjectName("respath_label")
        self.respath_label.setFont(font)
        self.horizontalLayout_4.addWidget(self.respath_label)
        self.respath_LE = QtWidgets.QLineEdit(self.layoutWidget)
        self.respath_LE.setObjectName("respath_LE")
        self.respath_LE.setFont(font_le)
        self.respath_LE.setMinimumHeight(30)
        self.respath_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_4.addWidget(self.respath_LE)
        self.path_tbtn = QtWidgets.QToolButton(self.layoutWidget)
        self.path_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.path_tbtn.setObjectName("path_tbtn")
        self.horizontalLayout_4.addWidget(self.path_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        # 序列文件
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.xvlieLB = QtWidgets.QLabel(self.layoutWidget)
        self.xvlieLB.setObjectName("xvlieLB")
        self.xvlieLB.setFont(font)
        self.horizontalLayout_3.addWidget(self.xvlieLB)
        self.xvlieLE = QtWidgets.QLineEdit(self.layoutWidget)
        self.xvlieLE.setObjectName("xvlieLE")
        self.xvlieLE.setFont(font_le)
        self.xvlieLE.setMinimumHeight(30)
        self.xvlieLE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_3.addWidget(self.xvlieLE)
        self.xvlieTbtn = QtWidgets.QToolButton(self.layoutWidget)
        self.xvlieTbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.xvlieTbtn.setObjectName("xvlieTbtn")
        self.horizontalLayout_3.addWidget(self.xvlieTbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        # 样品名称
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.sampleLB = QtWidgets.QLabel(self.layoutWidget)
        self.sampleLB.setObjectName("sampleLB")
        self.sampleLB.setFont(font)
        self.horizontalLayout_2.addWidget(self.sampleLB)
        self.sampleLE = QtWidgets.QLineEdit(self.layoutWidget)
        self.sampleLE.setObjectName("sampleLE")
        self.sampleLE.setFont(font_le)
        self.sampleLE.setFixedSize(QtCore.QSize(300, 30))
        self.horizontalLayout_2.addWidget(self.sampleLE)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        # 测序深度
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.depthLB = QtWidgets.QLabel(self.layoutWidget)
        self.depthLB.setObjectName("depthLB")
        self.depthLB.setFont(font)
        self.horizontalLayout.addWidget(self.depthLB)
        self.depthLE = QtWidgets.QLineEdit(self.layoutWidget)
        self.depthLE.setObjectName("depthLE")
        self.depthLE.setFont(font_le)
        self.depthLE.setFixedSize(QtCore.QSize(300, 30))
        self.horizontalLayout.addWidget(self.depthLE)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.run_btn.clicked.connect(self.receive_param)
        self.run_btn.clicked.connect(self.send_start_sig)
        self.cancel_btn.clicked.connect(Dialog.close)
        self.fastq_tbtn.clicked.connect(partial(self.open_file, self.fastq_LE))
        self.path_tbtn.clicked.connect(partial(self.choose_path, self.respath_LE))
        self.xvlieTbtn.clicked.connect(partial(self.open_file, self.xvlieLE))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.run_btn.setText(_translate("Dialog", "运行"))
        self.cancel_btn.setText(_translate("Dialog", "取消"))
        self.fastq_label.setText(_translate("Dialog", "选择fastq文件："))
        self.fastq_tbtn.setText(_translate("Dialog", "..."))
        self.respath_label.setText(_translate("Dialog", "选择结果文件存放路径："))
        self.path_tbtn.setText(_translate("Dialog", "..."))
        self.xvlieLB.setText(_translate("Dialog", "选择参考序列文件："))
        self.xvlieTbtn.setText(_translate("Dialog", "..."))
        self.sampleLB.setText(_translate("Dialog", "样品名称："))
        self.depthLB.setText(_translate("Dialog", "测序深度："))

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
        # fastq文件
        fastq_file = self.fastq_LE.text()
        # 结果路径
        result_file = self.respath_LE.text()
        # 样品名称、结果文件名称
        file_nm = self.sampleLE.text()
        # 序列文件路径
        xvlie_path = self.xvlieLE.text()
        # 测序深度
        depth = self.depthLE.text()

        # 判断fasta文件中的第一个字符为'>'并且有且仅有一个
        with open(xvlie_path, 'r') as f:
            file_content = f.read()
        findex = file_content.find('>')
        count = file_content.count('>')

        if not fastq_file:
            QMessageBox.warning(self, "警告", "请输入指定fasta文件！", QMessageBox.Ok)
        elif findex != 0 or count != 1:
            QMessageBox.warning(self, "警告", "fasta文件格式有误！", QMessageBox.Ok)
        elif not result_file:
            QMessageBox.warning(self, "警告", "请输入结果文件存放路径！", QMessageBox.Ok)
        elif not file_nm:
            QMessageBox.warning(self, "警告", "请输入结果文件名称！", QMessageBox.Ok)
        elif not xvlie_path:
            QMessageBox.warning(self, "警告", "请输入指定参考序列文件！", QMessageBox.Ok)
        elif not depth:
            QMessageBox.warning(self, "警告", "请输入指定测序深度！", QMessageBox.Ok)
        else:
            self.signal = 1
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 由于主页面需要显示（样品名称、barcode）参数，所以在子页面这两个参数必须存在
            parmas = {
                'task_type': task_type,
                'task_name': file_nm,
                'xvlie_path': xvlie_path,
                'count': depth,
                'sample_list': '',
                'barcode_list': '',
                'fastq_file': fastq_file,
                'work_file': result_file}
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

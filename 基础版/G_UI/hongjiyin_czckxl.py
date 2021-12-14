# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'czckxl.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
"""
宏基因组-查找参考序列条件页面输入各个必要的文件夹
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
        self.widget.setGeometry(QtCore.QRect(30, 20, 600, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # fastq文件条件
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(52, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.fastq_label = QtWidgets.QLabel(self.widget)
        self.fastq_label.setObjectName("fastq_label")
        self.fastq_label.setFont(font)
        self.horizontalLayout.addWidget(self.fastq_label)
        self.fastq_LE = QtWidgets.QLineEdit(self.widget)
        self.fastq_LE.setObjectName("fastq_LE")
        self.fastq_LE.setMinimumHeight(30)
        # self.fastq_LE.setFixedSize(QtCore.QSize(350, 30))
        self.fastq_LE.setFont(font_le)
        # 设置输入框禁止输入
        self.fastq_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.fastq_LE)
        self.fastq_tbtn = QtWidgets.QToolButton(self.widget)
        self.fastq_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.fastq_tbtn.setObjectName("fastq_tbtn")
        self.horizontalLayout.addWidget(self.fastq_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 结果文件路径选择
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.respath_label = QtWidgets.QLabel(self.widget)
        self.respath_label.setObjectName("respath_label")
        self.respath_label.setFont(font)
        self.horizontalLayout_2.addWidget(self.respath_label)
        self.respath_LE = QtWidgets.QLineEdit(self.widget)
        self.respath_LE.setObjectName("respath_LE")
        self.respath_LE.setMinimumHeight(30)
        # self.respath_LE.setFixedSize(QtCore.QSize(350, 30))
        self.respath_LE.setFont(font_le)
        # 设置输入框禁止输入
        self.respath_LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_2.addWidget(self.respath_LE)
        self.path_tbtn = QtWidgets.QToolButton(self.widget)
        self.path_tbtn.setMaximumSize(QtCore.QSize(30, 28))
        self.path_tbtn.setObjectName("path_tbtn")
        self.horizontalLayout_2.addWidget(self.path_tbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 结果文件名称
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.resfile_label = QtWidgets.QLabel(self.widget)
        self.resfile_label.setObjectName("resfile_label")
        self.resfile_label.setFont(font)
        self.horizontalLayout_3.addWidget(self.resfile_label)
        self.resfile_LE = QtWidgets.QLineEdit(self.widget)
        self.resfile_LE.setObjectName("resfile_LE")
        self.resfile_LE.setFixedSize(QtCore.QSize(150, 30))
        self.resfile_LE.setFont(font_le)
        self.horizontalLayout_3.addWidget(self.resfile_LE)
        spacerItem2 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # 数量
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.count_label = QtWidgets.QLabel(self.widget)
        self.count_label.setObjectName("count_label")
        self.count_label.setFont(font)
        self.horizontalLayout_4.addWidget(self.count_label)
        self.count_LE = QtWidgets.QLineEdit(self.widget)
        self.count_LE.setObjectName("count_LE")
        self.count_LE.setFixedSize(QtCore.QSize(150, 30))
        self.count_LE.setFont(font_le)
        self.horizontalLayout_4.addWidget(self.count_LE)
        spacerItem4 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.run_btn.clicked.connect(self.receive_param)
        self.run_btn.clicked.connect(self.send_start_sig)
        self.cancel_btn.clicked.connect(Dialog.close)
        self.fastq_tbtn.clicked.connect(partial(self.open_file, self.fastq_LE))
        self.path_tbtn.clicked.connect(partial(self.choose_path, self.respath_LE))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.run_btn.setText(_translate("Dialog", "运行"))
        self.cancel_btn.setText(_translate("Dialog", "取消"))
        self.fastq_label.setText(_translate("Dialog", "选择fastq文件："))
        self.fastq_tbtn.setText(_translate("Dialog", "..."))
        self.respath_label.setText(_translate("Dialog", "选择结果文件存放路径："))
        self.path_tbtn.setText(_translate("Dialog", "..."))
        self.resfile_label.setText(_translate("Dialog", "输入结果文件名称："))
        self.count_label.setText(_translate("Dialog", "数量："))

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
        # 结果文件名称
        file_nm = self.resfile_LE.text()
        # 数量
        count = self.count_LE.text()

        if not fastq_file:
            QMessageBox.warning(self, "警告", "请输入指定fastq文件！", QMessageBox.Ok)
        elif not result_file:
            QMessageBox.warning(self, "警告", "请输入结果文件存放路径！", QMessageBox.Ok)
        elif not file_nm:
            QMessageBox.warning(self, "警告", "请输入结果文件名称！", QMessageBox.Ok)
        elif not count:
            QMessageBox.warning(self, "警告", "请输入指定数量！", QMessageBox.Ok)
        else:
            self.signal = 1
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 由于主页面需要显示（样品名称、barcode）参数，所以在子页面这两个参数必须存在
            parmas = {
                'task_type': task_type,
                'task_name': file_nm,
                'xvlie_path': '',
                'count': count,
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

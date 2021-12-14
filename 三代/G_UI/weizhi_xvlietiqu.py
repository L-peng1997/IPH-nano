# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xvlietiqu.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
"""
未知病原输入各个必要的文件夹
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
        Dialog.setFixedSize(700, 550)

        # 设置字体
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(62, 20, 541, 71))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 30))
        self.lineEdit.setFont(font)
        self.verticalLayout.addWidget(self.lineEdit)

        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(60, 90, 251, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        font1 = QtGui.QFont()
        font1.setPointSize(9)
        # font1.setWeight(75)
        self.label_2.setFont(font1)
        self.horizontalLayout.addWidget(self.label_2)

        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{\n"
                                        "    background:#D3D3D3;\n"
                                        "    color:black;\n"
                                        "    border:1px groove gray;\n"
                                        "    padding:2px 4px;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:18px;border-radius: 3px;font-family: 思源黑体;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#A9A9A9;\n"
                                        "}\n")
        # self.pushButton.setStyleSheet("border:2px groove gray;border-radius:2px;padding:2px 4px;")
        self.horizontalLayout.addWidget(self.pushButton)

        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(110, 460, 431, 30))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background:#2AC28F;\n"
                                        "    color:white;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#99CC99;\n"
                                        "}\n")
        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    background:rgb(241, 84, 84);\n"
                                        "    color:white;\n"
                                        "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                        "}\n"
                                        "QPushButton:hover{                    \n"
                                        "    background:#FF6666;\n"
                                        "}\n")
        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.widget3 = QtWidgets.QWidget(Dialog)
        self.widget3.setGeometry(QtCore.QRect(60, 360, 431, 32))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.label_6 = QtWidgets.QLabel(self.widget3)
        self.label_6.setFixedSize(QtCore.QSize(210, 30))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font)
        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_5.setFixedSize(QtCore.QSize(200, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setFont(font)
        self.horizontalLayout_6.addWidget(self.lineEdit_5)

        self.widget4 = QtWidgets.QWidget(Dialog)
        self.widget4.setGeometry(QtCore.QRect(60, 150, 591, 186))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFixedSize(QtCore.QSize(220, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setFont(font)
        # 设置输入框禁止输入
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.toolButton = QtWidgets.QToolButton(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setFixedSize(QtCore.QSize(30, 25))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFixedSize(QtCore.QSize(220, 30))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)
        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setFont(font)
        # 设置输入框禁止输入
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.toolButton_2 = QtWidgets.QToolButton(self.widget4)
        self.toolButton_2.setFixedSize(QtCore.QSize(30, 25))
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget4)
        self.label_5.setFixedSize(QtCore.QSize(220, 30))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font)
        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.toolButton_3 = QtWidgets.QToolButton(self.widget4)
        self.toolButton_3.setFixedSize(QtCore.QSize(30, 25))
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_4.addWidget(self.toolButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(partial(self.open_file, self.lineEdit))
        self.pushButton_2.clicked.connect(self.receive_param)
        self.pushButton_2.clicked.connect(self.send_start_sig)
        self.pushButton_3.clicked.connect(Dialog.close)
        self.toolButton.clicked.connect(partial(self.open_file, self.lineEdit_2))
        self.toolButton_2.clicked.connect(partial(self.open_file, self.lineEdit_3))
        self.toolButton_3.clicked.connect(partial(self.choose_path, self.lineEdit_4))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "请在下方输入指定txid:"))
        self.label_2.setText(_translate("Dialog", "或选择指定的txid列表文件"))
        self.pushButton.setText(_translate("Dialog", "浏览"))
        self.pushButton_2.setText(_translate("Dialog", "运行"))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.label_6.setText(_translate("Dialog", "输入结果文件名称："))
        self.label_3.setText(_translate("Dialog", "选择fastq文件:"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.label_4.setText(_translate("Dialog", "选择分类文件:"))
        self.toolButton_2.setText(_translate("Dialog", "..."))
        self.label_5.setText(_translate("Dialog", "选择结果文件存放路径："))
        self.toolButton_3.setText(_translate("Dialog", "..."))

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
        # txid
        txid = self.lineEdit.text()
        # fastq文件
        fastq_file = self.lineEdit_2.text()
        # tsv文件
        tsv_file = self.lineEdit_3.text()
        # 结果路径
        result_file = self.lineEdit_4.text()
        # 结果文件名称
        file_nm = self.lineEdit_5.text()

        if not txid:
            QMessageBox.warning(self, "警告", "请输入指定txid！", QMessageBox.Ok)
            # print(reply)
        elif not fastq_file:
            QMessageBox.warning(self, "警告", "请输入指定fastq文件！", QMessageBox.Ok)
            # print(reply)
        elif not tsv_file:
            QMessageBox.warning(self, "警告", "请输入指定tsv文件！", QMessageBox.Ok)
            # print(reply)
        elif not result_file:
            QMessageBox.warning(self, "警告", "请输入结果文件存放路径！", QMessageBox.Ok)
            # print(reply)
        elif not file_nm:
            QMessageBox.warning(self, "警告", "请输入结果文件名称！", QMessageBox.Ok)
        else:
            self.signal = 1
            # 以当前时间戳作为任务名
            # task_name = str(int(time.time()))
            # 以起始文件路径的最后一个文件夹名称作为任务名
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 结果文件存放路径
            # print(file_path, self.sample_list, self.barcode_list)
            # parmas = [task_type, task_name, self.sample_list, self.barcode_list, file_path]
            parmas = {
                'task_type': task_type,
                'task_name': file_nm,
                'sample_list': '',
                'barcode_list': '',
                'txid': txid,
                'fastq_file': fastq_file,
                'tsv_file': tsv_file,
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

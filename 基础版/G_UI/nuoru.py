# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
"""
界面只需要输入文件夹路径
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QDialog
from configparser import ConfigParser
import os
import sys


# base_path = app_path().replace('\\', '/')
base_path = os.getcwd()
config = ConfigParser()
config.read(f'{base_path}/G_CONFIG/config.ini', encoding='utf-8')


class Ui_Dialog(QWidget):
    paramSignal = pyqtSignal(dict)
    startSignal = pyqtSignal(int)
    signal = 0

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.sample_list = []
        self.barcode_list = []

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(720, 300)
        # Dialog.setStyleSheet("background:#F5F5F5;")
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 200, 366, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.commitButton = QtWidgets.QPushButton(self.layoutWidget)
        self.commitButton.setStyleSheet("QPushButton{\n"
                                      "    background:#2AC28F;\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#99CC99;\n"
                                      "}\n")
        self.commitButton.setFixedSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.commitButton.setFont(font)
        self.commitButton.setObjectName("commitButton")
        self.horizontalLayout_3.addWidget(self.commitButton)
        spacerItem = QtWidgets.QSpacerItem(150, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelButton.setStyleSheet("QPushButton{\n"
                                      "    background:#FF6666;\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#FF6666;\n"
                                      "}\n")
        self.cancelButton.setFixedSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 40, 658, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setPlaceholderText('请输入起始文件夹上级路径')
        self.lineEdit.setStyleSheet(
                                '''QLineEdit{
                                        border:1px solid gray;
                                        width:300px;
                                        border-radius:5px;
                                        padding:2px 4px;
                                }''')
        self.lineEdit.setFixedSize(QtCore.QSize(600, 40))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        # 设置输入框禁止输入
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget1)
        self.toolButton.setFixedSize(QtCore.QSize(35, 30))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.close)
        self.commitButton.clicked.connect(self.receive_param)
        self.commitButton.clicked.connect(self.send_start_sig)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.commitButton.setText(_translate("Dialog", "运行"))
        self.cancelButton.setText(_translate("Dialog", "取消"))
        self.label.setText(_translate("Dialog", "请选择文件路径："))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.toolButton.clicked.connect(self.open_file)

    def open_file(self):
        """
        设置起始文件夹路径
        :return:
        """
        directory1 = QFileDialog.getExistingDirectory(self, "选取文件", "./")
        self.lineEdit.setText(directory1)

    def receive_param(self):
        """
        接收子窗口中的所有参数，并发送给主窗口
        :return: 当前工作路径
        """
        file_path = self.lineEdit.text()
        if not self.lineEdit.text():
            QMessageBox.warning(self, "警告", "目表文件路径不能为空！", QMessageBox.Ok)
        else:
            self.signal = 1
            # 以当前时间戳作为任务名
            # task_name = str(int(time.time()))
            # 以起始文件路径的最后一个文件夹名称作为任务名
            task_name = file_path.split('/')[-1]
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 结果文件存放路径
            # 诺如病毒、相似序列查找、分子进化树默认放在当前路径下
            # work_file = config.get('SARS-COV-2', 'work_file')
            work_file = file_path
            parmas = {
                'task_type': task_type,
                'task_name': task_name,
                'sample_list': '',
                'barcode_list': '',
                'file_path': file_path,
                'work_file': work_file}
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


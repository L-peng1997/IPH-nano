# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
"""
新冠测序界面，需要输入文件夹路径、样品名称、barcode等参数
"""
import sys
import qtawesome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QDialog
from configparser import ConfigParser
import os


# base_path = app_path().replace('\\', '/')
base_path = os.getcwd().replace('\\', '/')
config = ConfigParser()
config.read(f'{base_path}/G_CONFIG/config.ini', encoding='utf-8')


class Ui_Dialog(QWidget):
    paramSignal = pyqtSignal(dict)
    startSignal = pyqtSignal(int)
    signal = 0

    def __init__(self, current_tree):
        super(Ui_Dialog, self).__init__()
        self.sample_list = []
        self.barcode_list = []
        self.current_tree = current_tree

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(720, 630)
        # Dialog.setStyleSheet("background:#F5F5F5;")
        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 510, 366, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                      "    background:#2AC28F;\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#99CC99;\n"
                                      "}\n")
        self.pushButton_2.setFixedSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(150, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                      "    background:rgb(241, 84, 84);\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#FF6666;\n"
                                      "}\n")
        self.pushButton_3.setFixedSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
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
                                        font-weight:bold;
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
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(12, 151, 174, 42))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                      "    background:#2AC28F;\n"
                                      "    color:white;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#3CB371;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background:#99CC99;\n"
                                      "    border: 1px solid #3C3C3C!important;\n"
                                      "}")
        self.pushButton_4.setFixedSize(QtCore.QSize(150, 40))
        self.pushButton_4.setFont(self.font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(11, 211, 701, 252))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFixedSize(QtCore.QSize(630, 250))
        self.tableWidget.setFont(self.font)
        self.tableWidget.setLineWidth(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionsClickable(False)
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:#F0F3F6;}")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        for i in range(3):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.close)
        self.pushButton_2.clicked.connect(self.receive_param)
        self.pushButton_2.clicked.connect(self.send_start_sig)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "运行"))
        self.pushButton_3.setText(_translate("Dialog", "取消"))
        self.label.setText(_translate("Dialog", "请选择文件路径："))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.toolButton.clicked.connect(self.open_file)
        self.pushButton_4.setText(_translate("Dialog", "添加样品"))
        self.pushButton_4.clicked.connect(self.add_param)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "样品名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "标签名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "操作"))
        self.table_add_widget(0)

    def add_param(self):
        row_num = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_num + 1)
        self.table_add_widget(row_num)

    def table_add_widget(self, rowNum):
        # 下拉框
        self.tableWidget.verticalHeader().setVisible(False)
        addtask_icon = qtawesome.icon('fa.plus-square', color='white')
        comBox = QtWidgets.QComboBox()
        content = ['']
        for i in range(1, 25):
            if i < 10:
                i = str(i).zfill(2)
            content.append(f'barcode{i}')
        comBox.addItems(content)
        comBox.setFont(self.font)
        # comBox.setAlignment(QtCore.Qt.AlignCenter)
        comBox.setStyleSheet("QComboBox {"
                                    "combobox-popup: 0;\n"  # 滚动条设置必需
                                    "border-style:none; "
                                    "width:48px; "
                                    "height:24px; "
                                    "padding-left:60%; "
                                    "background: #ffffff; "
                                    "line-height:24px; }\n"

                                    "QComboBox:drop-down {"  # 选择箭头样式
                                    "width:40px;  "
                                    "height:50px; "
                                    "border: 5px;  "
                                    # "background: #ffffff; " 
                                    "subcontrol-origin: padding;}\n"  # 对齐方式

                                    "QComboBox QAbstractItemView {"  # 下拉选项样式
                                    "color:black; "
                                    "background: transparent; "
                                    "selection-color:rgba(93,169,255,1);"
                                    "selection-background-color: rgba(255,255,255,1);"
                                    "}\n"

                                    "QComboBox QAbstractScrollArea QScrollBar:vertical {"  # 滚动条样式
                                    "width: 6px;\n"
                                    "height: 100px;"
                                    "background-color: transparent;  }\n"

                                    "QComboBox QAbstractScrollArea QScrollBar::handle:vertical {\n"  # 滚动条样式
                                    "border-radius: 3px;   "
                                    "background: rgba(0,0,0,0.1);}\n"

                                    # "QComboBox QAbstractScrollArea QScrollBar::handle:vertical:hover {\n"  # 划过滚动条，变化
                                    # "background: rgb(90, 91, 93);}\n"

                                    "QComboBox QScrollBar::add-line::vertical{"  # 滚动条上箭头
                                    "border:none;}"
                                    "QComboBox QScrollBar::sub-line::vertical{"  # 滚动条下箭头
                                    "border:none;}"
                                    "")
        comBox.setMaximumSize(200, 100)
        # 设置最大可见数为8
        comBox.setMaxVisibleItems(6)
        # comBox.currentIndexChanged.connect(self.comBoxSelect)
        self.tableWidget.setCellWidget(rowNum, 1, comBox)
        # 输入框
        sample_ = QtWidgets.QLineEdit()
        sample_.setAlignment(QtCore.Qt.AlignCenter)
        sample_.setStyleSheet('QLineEdit{font-size:18px;border-style:none;};')
        sample_.setPlaceholderText('请输入样品名称')
        self.tableWidget.setCellWidget(rowNum, 0, sample_)
        # 设置表格行自动变色
        btn_icon = qtawesome.icon('fa.trash-o', color='white')
        btn = QtWidgets.QPushButton(btn_icon, '删除')
        btn.setStyleSheet("QPushButton{\n"
                          "    color:White;\n"
                          "    font-family:思源黑体;\n"
                          "    border: 5px;\n"
                          "    background:#FF6666;font-size:18px;border-radius: 5px;margin:2px 45px 2px 45px;\n"
                          "}\n"
                          "QPushButton:hover{\n"
                          "    background:#FF0033;\n"
                          "}\n"
                          "QPushButton:pressed{\n"
                          "    background:#CC3333;\n"
                          "}")
        btn.clicked.connect(self.del_data)
        self.tableWidget.setCellWidget(rowNum, 2, btn)

    def comBoxSelect(self, index):
        print(f'当前选择的数据在下拉列表中的索引为{index}')

    def del_data(self):
        """
        点击按钮删除表格的当前行
        :return:
        """
        button = self.sender()
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()
            self.tableWidget.removeRow(row)

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
        row_num = self.tableWidget.rowCount()
        self.sample_list.clear()
        self.barcode_list.clear()
        for i in range(row_num):
            sample_name = self.tableWidget.cellWidget(i, 0).text() if self.tableWidget.cellWidget(i, 0).text() else ''
            self.sample_list.append(sample_name)
            barcode_num = self.tableWidget.cellWidget(i, 1).currentText()
            self.barcode_list.append(barcode_num)

        if not self.lineEdit.text():
            QMessageBox.warning(self, "警告", "目表文件路径不能为空！", QMessageBox.Ok)
            # print(reply)
        elif len(set(self.barcode_list)) != len(self.barcode_list):
            QMessageBox.warning(self, "警告", "barcode参数\n有重复值！", QMessageBox.Ok)
            # print(reply)
        elif len(set(self.sample_list)) != len(self.sample_list):
            QMessageBox.warning(self, "警告", "样品名称\n有重复值！", QMessageBox.Ok)
            # print(reply)
        elif '' in self.sample_list or '' in self.barcode_list:
            QMessageBox.warning(self, "警告", "参数不能为空！", QMessageBox.Ok)
            # print(reply)
        else:
            self.signal = 1
            # 以当前时间戳作为任务名
            # task_name = str(int(time.time()))
            # 以起始文件路径的最后一个文件夹名称作为任务名
            task_name = file_path.split('/')[-1]
            # 获取当前窗口标题进行任务区分
            task_type = self.Dialog.windowTitle()
            # 结果文件存放路径
            if self.current_tree == '新冠病毒' or self.current_tree == '测序':
                work_file = config.get('SARS-COV-2', 'work_file')
            elif self.current_tree == '未知病原':
                work_file = config.get('Unknown_Path', 'work_file')
            # print(file_path, self.sample_list, self.barcode_list)
            # parmas = [task_type, task_name, self.sample_list, self.barcode_list, file_path]
            parmas = {
                'task_type': task_type,
                'task_name': task_name,
                'sample_list': self.sample_list,
                'barcode_list': self.barcode_list,
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
    main_ui = Ui_Dialog('测序')
    main_ui.setupUi(main)
    # 显示
    main.show()
    # QMessageBox.warning()
    sys.exit(app.exec_())

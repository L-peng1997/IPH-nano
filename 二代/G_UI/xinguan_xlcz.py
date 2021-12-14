# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xvliechazhao.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
"""
新冠序列查找界面，需要输入文件夹路径、程序运行参数
（界面根据文件夹路径自动生成程序运行的参数）
"""
import qtawesome
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QApplication, QDialog
from PyQt5.QtGui import QIcon
from configparser import ConfigParser
import os
import re
import pandas as pd
from datetime import date
import subprocess

# base_path = app_path().replace('\\', '/')
base_path = os.getcwd().replace('\\', '/')
config = ConfigParser()
config.read(f'{base_path}/G_CONFIG/config.ini', encoding='utf-8')


class Ui_Dialog(QWidget):
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
        Dialog.setFixedSize(850, 600)
        # Dialog.setStyleSheet("background:#F5F5F5;")
        self.font = QtGui.QFont()
        self.font.setPointSize(12)

        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 110, 400, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.count = QtWidgets.QLabel(self.layoutWidget)
        self.count.setObjectName("count")
        self.count.setFont(self.font)
        self.horizontalLayout_2.addWidget(self.count)
        self.count_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.count_lineEdit.sizePolicy().hasHeightForWidth())
        self.count_lineEdit.setSizePolicy(sizePolicy)
        self.count_lineEdit.setFixedSize(QtCore.QSize(200, 35))
        self.count_lineEdit.setObjectName("count_lineEdit")
        self.count_lineEdit.setFont(self.font)
        self.count_lineEdit.setText('500')
        self.horizontalLayout_2.addWidget(self.count_lineEdit)

        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 180, 750, 300))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.add_Btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.add_Btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.add_Btn.setObjectName("add_Btn")
        self.add_Btn.setStyleSheet("QPushButton{\n"
                                   "    background:#2AC28F;\n"
                                   "    color:white;\n"
                                   "    height:40px;\n"
                                   "    width:150px;\n"
                                   "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                   "}\n"
                                   "QPushButton:hover{                    \n"
                                   "    background:#99CC99;\n"
                                   "}\n"
                                   "QPushButton:pressed{\n"
                                   "    background:#8FBC8F;\n"
                                   "    border: 1px solid #3C3C3C!important;\n"
                                   "}")
        # 2021-08-15 10:37:31 修改按钮对齐方式，使其靠左对齐
        self.horizontalLayout_4.addWidget(self.add_Btn, alignment=QtCore.Qt.AlignLeft)
        # 2021-08-15 10:35:34
        # 去掉升级数据库的按钮
        # self.upgrade_Btn = QtWidgets.QPushButton(self.layoutWidget1)
        # self.upgrade_Btn.setMaximumSize(QtCore.QSize(150, 16777215))
        # self.upgrade_Btn.setObjectName("upgrade_Btn")
        # self.upgrade_Btn.setStyleSheet("QPushButton{\n"
        #                                "    background:#FF0000;\n"
        #                                "    color:white;\n"
        #                                "    height:40px;\n"
        #                                "    width:200px;\n"
        #                                "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;font-weight:bold;border-radius: 3px;font-family: 思源黑体;\n"
        #                                "}\n"
        #                                "QPushButton:hover{                    \n"
        #                                "    background:#DC143C;\n"
        #                                "}\n"
        #                                "QPushButton:pressed{\n"
        #                                "    background:#B22222;\n"
        #                                "    border: 1px solid #3C3C3C!important;\n"
        #                                "}")
        # self.horizontalLayout_4.addWidget(self.upgrade_Btn, alignment=QtCore.Qt.AlignRight)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.sample_table = QtWidgets.QTableWidget(self.layoutWidget1)
        self.sample_table.setObjectName("sample_table")
        self.sample_table.setColumnCount(6)
        self.sample_table.setRowCount(1)
        self.sample_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.sample_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.sample_table.horizontalHeader().setFixedHeight(35)
        # self.sample_table.horizontalHeader().setSectionsClickable(False)
        self.sample_table.horizontalHeader().setStyleSheet("QHeaderView::section{background:#F0F3F6;}")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        # font.setWeight(30)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        # self.sample_table.setVerticalHeaderItem(0, item)
        for i in range(6):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.sample_table.setHorizontalHeaderItem(i, item)
        self.verticalLayout_2.addWidget(self.sample_table)
        self.verticalLayout_2.addWidget(self.sample_table)

        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(140, 500, 531, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_Btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.start_Btn.setFixedSize(QtCore.QSize(100, 35))
        self.start_Btn.setObjectName("start_Btn")
        self.start_Btn.setStyleSheet("QPushButton{\n"
                                     "    background:#2AC28F;\n"
                                     "    color:white;\n"
                                     "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                     "}\n"
                                     "QPushButton:hover{                    \n"
                                     "    background:#99CC99;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background:#8FBC8F;\n"
                                     "    border: 1px solid #3C3C3C!important;\n"
                                     "}"
                                     )
        self.horizontalLayout_3.addWidget(self.start_Btn)
        self.close_Btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.close_Btn.setFixedSize(QtCore.QSize(100, 35))
        self.close_Btn.setObjectName("close_Btn")
        self.close_Btn.setStyleSheet("QPushButton{\n"
                                     "    background:rgb(241, 84, 84);\n"
                                     "    color:white;\n"
                                     "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                     "}\n"
                                     "QPushButton:hover{                    \n"
                                     "    background:#FA8072;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "    background:#CD5C5C;\n"
                                     "    border: 1px solid #3C3C3C!important;\n"
                                     "}"
                                     )
        self.horizontalLayout_3.addWidget(self.close_Btn)

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(51, 31, 750, 65))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.path = QtWidgets.QLabel(self.widget)
        self.path.setObjectName("path")
        self.verticalLayout.addWidget(self.path)
        self.path.setFont(self.font)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path_lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_lineEdit.sizePolicy().hasHeightForWidth())
        self.path_lineEdit.setSizePolicy(sizePolicy)
        self.path_lineEdit.setMinimumSize(QtCore.QSize(500, 35))
        self.path_lineEdit.setObjectName("path_lineEdit")
        self.path_lineEdit.setFont(self.font)
        # 设置输入框禁止输入
        self.path_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.path_lineEdit)
        self.path_tBtn = QtWidgets.QToolButton(self.widget)
        self.path_tBtn.setFixedSize(QtCore.QSize(40, 35))
        self.path_tBtn.setObjectName("path_tBtn")
        self.horizontalLayout.addWidget(self.path_tBtn)
        self.path_Btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_Btn.sizePolicy().hasHeightForWidth())
        self.path_Btn.setSizePolicy(sizePolicy)
        self.path_Btn.setFixedSize(QtCore.QSize(100, 35))
        self.path_Btn.setObjectName("path_Btn")
        self.path_Btn.setStyleSheet("QPushButton{\n"
                                    "    background:#2AC28F;\n"
                                    "    color:white;\n"
                                    "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 3px;font-family: 思源黑体;\n"
                                    "}\n"
                                    "QPushButton:hover{                    \n"
                                    "    background:#99CC99;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    background:#8FBC8F;\n"
                                    "    border: 1px solid #3C3C3C!important;\n"
                                    "}"
                                    )
        self.horizontalLayout.addWidget(self.path_Btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.path_tBtn.clicked.connect(self.open_file)
        self.path_Btn.clicked.connect(self.refush_table)
        self.add_Btn.clicked.connect(self.add_param)
        self.close_Btn.clicked.connect(Dialog.close)
        self.start_Btn.clicked.connect(self.receive_param)
        self.start_Btn.clicked.connect(self.send_start_sig)
        # 2021-08-15 10:35:34
        # 去掉升级数据库的按钮
        # self.upgrade_Btn.clicked.connect(Dialog.close)
        # self.upgrade_Btn.clicked.connect(self.update_database)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.count.setText(_translate("Dialog", "请输入待提取数量："))
        self.add_Btn.setText(_translate("Dialog", "添加样品"))
        # 2021-08-15 10:35:34
        # 去掉升级数据库的按钮
        # self.upgrade_Btn.setText(_translate("Dialog", "更新数据库"))
        self.start_Btn.setText(_translate("Dialog", "运行"))
        self.close_Btn.setText(_translate("Dialog", "取消"))
        self.path.setText(_translate("Dialog", "请选择文件路径："))
        self.path_tBtn.setText(_translate("Dialog", "..."))
        self.path_Btn.setText(_translate("Dialog", "提交"))
        # item = self.sample_table.verticalHeaderItem(0)
        # item.setText(_translate("Dialog", "1"))
        # item = self.sample_table.horizontalHeaderItem(0)
        # item.setText(_translate("Dialog", " "))
        item = self.sample_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "strain"))
        item = self.sample_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "date"))
        item = self.sample_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "region"))
        item = self.sample_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "country"))
        item = self.sample_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "location"))
        item = self.sample_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "操作"))
        # default_list = ['序列名称', 'XXXX-XX-XX', '', 'China', 'Guangzhou', '']
        # for i, xvlie in zip(range(self.tableWidget.rowCount()), default_list):
        self.table_add_widget(0, '序列名称')

    def refush_table(self):
        file_path = self.path_lineEdit.text()
        if not file_path:
            QMessageBox.warning(self, "警告", "目表文件路径不能为空！", QMessageBox.Ok)
        elif not os.path.exists(f'{file_path}/0.data'):
            QMessageBox.warning(self, "警告", "起始文件夹(0.data)不存在！", QMessageBox.Ok)
        elif not os.path.exists(f'{file_path}/0.data/sample.fa'):
            QMessageBox.warning(self, "警告", "缺失 sample.fa 文件！", QMessageBox.Ok)
        else:
            with open(f'{file_path}/0.data/sample.fa') as f:
                data = f.read()
            name_list = re.findall(r'>(.*?)\s+', data)
            for name_ in name_list:
                self.xvlie_list.append(name_)
            self.sample_table.setRowCount(len(self.xvlie_list))
            for i, sample in zip(range(self.sample_table.rowCount()), self.xvlie_list):
                self.table_add_widget(i, sample)

    def add_param(self):
        row_num = self.sample_table.rowCount()
        self.sample_table.setRowCount(row_num + 1)
        # default_list = ['序列名称', 'XXXX-XX-XX', '', 'China', 'Guangzhou', '']
        # for i, xvlie in zip(range(self.tableWidget.rowCount()), default_list):
        self.table_add_widget(row_num, '序列名称')

    def table_add_widget(self, rowNum, sample):

        # 表格首列添加勾选框
        # 若要添加勾选框，则应使表格新增一列
        # self.check = QtWidgets.QTableWidgetItem()
        # self.check.setCheckState(QtCore.Qt.Unchecked)
        # self.sample_table.setItem(rowNum, 0, self.check)

        sample_ = QtWidgets.QLineEdit()
        sample_.setStyleSheet('QLineEdit{margin:3px 10px 3px 10px;border:1px solid lightgray;border-radius:5px;'
                              'font-size:18px;font-family: 思源黑体;};')
        # sample_.setPlaceholderText(data)
        sample_.setText(sample)
        sample_.setToolTip(sample)
        self.sample_table.setCellWidget(rowNum, 0, sample_)

        time_line = QtWidgets.QLineEdit()
        time_line.setStyleSheet('QLineEdit{margin:3px 10px 3px 10px;border:1px solid lightgray;border-radius:5px;'
                                'font-size:18px;font-weight:bold;font-family: 思源黑体;};')
        time_line.setToolTip('XXXX-XX-XX:如果未知则用XX代替，如2020-01-XX')
        time_line.setText(str(date.today()))
        self.sample_table.setCellWidget(rowNum, 1, time_line)

        zhou_line = QtWidgets.QLineEdit()
        zhou_line.setStyleSheet('QLineEdit{margin:3px 10px 3px 10px;border:1px solid lightgray;border-radius:5px;'
                                'font-size:18px;font-weight:bold;font-family: 思源黑体;};')
        zhou_line.setText('Asia')
        self.sample_table.setCellWidget(rowNum, 2, zhou_line)

        coun_line = QtWidgets.QLineEdit()
        coun_line.setStyleSheet('QLineEdit{margin:3px 10px 3px 10px;border:1px solid lightgray;border-radius:5px;'
                                'font-size:18px;font-weight:bold;font-family: 思源黑体;};')
        coun_line.setText('China')
        self.sample_table.setCellWidget(rowNum, 3, coun_line)

        prov_line = QtWidgets.QLineEdit()
        prov_line.setStyleSheet('QLineEdit{margin:3px 10px 3px 10px;border:1px solid lightgray;border-radius:5px;'
                                'font-size:18px;font-weight:bold;font-family: 思源黑体;};')
        prov_line.setText('Guangdong')
        self.sample_table.setCellWidget(rowNum, 4, prov_line)

        btn_icon = qtawesome.icon('fa.trash-o', color='white')
        btn = QtWidgets.QPushButton(btn_icon, '删除')
        btn.setStyleSheet("QPushButton{\n"
                          "    color:White;\n"
                          "    font-family:思源黑体;\n"
                          "    border: 5px;\n"
                          "    background:#FF6666;font-size:18px;border-radius: 5px;margin:2px 5px 2px 5px;\n"
                          "}\n"
                          "QPushButton:hover{\n"
                          "    background:#FF0033;\n"
                          "}\n"
                          "QPushButton:pressed{\n"
                          "    background:#CC3333;\n"
                          "}")
        btn.clicked.connect(self.del_data)
        self.sample_table.setCellWidget(rowNum, 5, btn)

    def del_data(self):
        """
        点击按钮删除表格的当前行
        :return:
        """
        button = self.sender()
        if button:
            row = self.sample_table.indexAt(button.pos()).row()
            self.sample_table.removeRow(row)

    def open_file(self):
        """
        设置起始文件夹路径
        :return:
        """
        directory1 = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.path_lineEdit.setText(directory1)

    def receive_param(self):
        """
        接收子窗口中的所有参数，并发送给主窗口
        :return: 当前工作路径
        """
        file_path = self.path_lineEdit.text()
        if not file_path:
            QMessageBox.warning(self, "警告", "目表文件路径不能为空！", QMessageBox.Ok)
        elif not os.path.exists(f'{file_path}/0.data'):
            QMessageBox.warning(self, "警告", "起始文件夹(0.data)不存在！", QMessageBox.Ok)
        elif not os.path.exists(f'{file_path}/0.data/sample.fa'):
            QMessageBox.warning(self, "警告", "缺失 sample.fa 文件！", QMessageBox.Ok)
        elif not self.count_lineEdit.text():
            QMessageBox.warning(self, "警告", "请输入提取数量！", QMessageBox.Ok)
        else:
            row_num = self.sample_table.rowCount()
            col_num = self.sample_table.columnCount()
            self.data_list.clear()
            for row in range(row_num):
                row_list = []
                for col in range(col_num - 1):
                    # if col != 0:
                    data = self.sample_table.cellWidget(row, col).text()
                    # else:
                        # 0为不选择，2为选择。
                        # 其中1为部分选择，即介于全选和全不选之间的状态，例子可参考邮箱标记已读时最顶端勾选框状态
                        # data = self.sample_table.item(row, col).checkState()
                    row_list.append(data)
                self.data_list.append(row_list)
            # result = pd.concat(self.data_list)
            # 2021-08-16 11:15:03 去掉首列表格勾选框，不在写入到sample.tsv文件中
            # df = pd.DataFrame(self.data_list, columns=['ifcheck', 'strain', 'date', 'region', 'country', 'location'])
            df = pd.DataFrame(self.data_list, columns=['strain', 'date', 'region', 'country', 'location'])
            df['Accession ID'] = ['?'] * len(self.data_list)
            df['Clade'] = ['?'] * len(self.data_list)
            df['Pango lineage'] = ['?'] * len(self.data_list)
            order = ['strain', 'Accession ID', 'date', 'region', 'country', 'location',
                     'Clade', 'Pango lineage']
            df = df[order]

            if os.path.exists(f'{file_path}/0.data/sample.tsv'):
                os.remove(f'{file_path}/0.data/sample.tsv')
            df.to_csv(f'{file_path}/0.data/sample.tsv', index=False, sep='\t')

            if '' in self.data_list[0]:
                QMessageBox.warning(self, "警告", "参数不能为空！", QMessageBox.Ok)
            else:
                self.signal = 1
                # 获取提取数量
                count_ = self.count_lineEdit.text()
                # 以当前时间戳作为任务名
                # task_name = str(int(time.time()))
                # 以起始文件路径的最后一个文件夹名称作为任务名
                task_name = file_path.split('/')[-1] if '/' in file_path else file_path
                # 获取当前窗口标题进行任务区分
                task_type = self.Dialog.windowTitle()
                # task_type = '相似序列查找'
                # 结果文件存放路径
                # work_file = config.get('SARS-COV-2', 'work_file')
                work_file = file_path  # snakemake执行后会在脚本所在路径生成结果文件，故不需要指定结果文件夹
                parmas = {
                    'task_type': task_type,
                    'task_name': task_name,
                    'sample_list': '',
                    'barcode_list': '',
                    'file_path': file_path,
                    'work_file': work_file,
                    'count': count_}
                # print(parmas)
                self.paramSignal.emit(parmas)
                self.Dialog.close()

    def send_start_sig(self):
        # print(f'发送的信号为：{self.signal}')
        self.startSignal.emit(self.signal)

    def update_database(self):
        db_path = config.get('SARS2_analyze', 'database_path')

        # 执行wget命令
        wget1 = 'wget ftp://106.52.33.51/pub/Database/gisaid/gisaid.tsv.gz'
        wget2 = 'wget ftp://106.52.33.51/pub/Database/gisaid/gisaid.align.fa.xz'
        wget = wget1 + '&&' + wget2
        # 执行mv命令
        mv_comm1 = f'mv {db_path}/gisaid.align.fa {db_path}/backup'
        mv_comm2 = f'mv {db_path}/gisaid.tsv {db_path}/backup'
        mv_comm3 = f'mv gisaid.tsv.gz {db_path}'
        mv_comm4 = f'mv gisaid.align.fa.xz {db_path}'
        mv_comm = '&&'.join([mv_comm1, mv_comm2, mv_comm3, mv_comm4])

        gzip_comm = f'gzip -d {db_path}/gisaid.tsv.gz'

        xz_comm = f'xz -d {db_path}/gisaid.align.fa.xz'

        try:
            if not os.path.exists(db_path + '/' + 'backup'):
                os.mkdir(db_path + '/' + 'backup')
        except Exception as e:
            QMessageBox.warning(self, '警告', str(e), QMessageBox.Ok)
        else:
            try:
                status = []
                for comm in [wget, mv_comm, gzip_comm, xz_comm]:
                    print(f'正在执行命令{comm}')
                    result = subprocess.run(comm, shell=True, stderr=subprocess.PIPE, universal_newlines=True)
                    if result.returncode != 0:
                        raise Exception(result.stderr)
                    elif result.returncode == 0:
                        status.append(0)
                print(sum(status))
            except Exception as e:
                print(f'更新数据库失败：{e}')
                QMessageBox.warning(self, "警告", str(e), QMessageBox.Ok)


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

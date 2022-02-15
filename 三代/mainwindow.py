# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import os
import qtawesome
import re
import shutil
import sqlite3
import threading
import hashlib
from configparser import ConfigParser
from datetime import datetime
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, Qt, QTimer, QDateTime, pyqtSlot
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog, QToolTip
from G_COMM.runDatacontrol import RunDataControl
from G_COMM.runErdaixlpj import RunErdaixlpj
from G_COMM.runHongjiyin import RunHongjiyin
from G_COMM.runJinhuashu import RunJinhuashu
from G_COMM.runLiugan import RunLiugan
from G_COMM.runSnakemake import RunSnakemake
from G_COMM.runWeizhi import RunWeizhi
from G_COMM.runXinguan import RunCommand, logger
from G_COMM.runXvlietiqu import RunPython
# 2021-12-05 20:26:38 增加命令运行
from G_COMM.runPythonFile import RunPythonFile
from G_UI.erdai_xvliepj import Ui_Dialog as Erxlpj_UI
from G_UI.erdai_zhikong import Ui_Dialog as Zhikong_UI
from G_UI.hongjiyin_czckxl import Ui_Dialog as Czckxl_UI
from G_UI.hongjiyin_xlpj import Ui_Dialog as Xlpj_UI
from G_UI.liugan import Ui_Dialog as Liugan_UI
from G_UI.nuoru import Ui_Dialog as Nuoru_Ui
from G_UI.weizhi_xvlietiqu import Ui_Dialog as Xvlietiqu_UI
from G_UI.xinguan_xlpj import Ui_Dialog as Xinguan_Ui
from G_UI.xinguan_suyuan import Ui_Dialog as Xvlie_UI
# 2021-12-05 19:47:47 添加界面
from G_UI.weizhi_xlfl import Ui_Dialog as WZxlfl_UI
from G_UI.erdai_ctpj import Ui_Dialog as EDctpj_UI
from G_UI.hongjiyin_ctpj import Ui_Dialog as HJYctpj_UI
from createDB import build_db
from drawZhex import QtDraw
from webShow import WebShow

# 项目路径
# base_path = app_path().replace('\\', '/')
base_path = os.getcwd().replace('\\', '/')
config = ConfigParser()
config.read(f'{base_path}/G_CONFIG/config.ini', encoding='utf-8')

# 当前路径
# base_path = os.getcwd().replace('\\', '/')


class Ui_MainWindow(QObject):

    def __init__(self):
        super().__init__()
        # 程序参数
        self.params = dict()
        # 程序状态
        self.status = ''
        # 数据库连接
        build_db()
        self.conn = sqlite3.connect(f'{base_path}/sequence.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

        # 初始化一个定时器
        self.timer = QTimer()
        # 定时器结束，触发showTime方法
        self.timer.timeout.connect(self.showTime)
        # 定义开始时间
        self.start_time = ''

        # 诺如结果文件夹列表
        nuoru_result_file = config.get('Norovirus', 'result_file')
        self.nuoru_file_list = nuoru_result_file.split(',')

        # 新冠序列分析结果文件夹列表
        xg_analyse_result_file = config.get('SARS2_analyze', 'result_file')
        self.xg_analyse_file_list = xg_analyse_result_file.split(',')

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")

        MainWindow.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        # MainWindow.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # MainWindow.setWindowOpacity(0.9)               # 设置窗口透明度

        # 设置窗口图标
        MainWindow.setWindowIcon(QIcon(f'{base_path}/img/logo.png'))
        # 窗口背景色
        # MainWindow.setStyleSheet("background:#FFFFFF;")
        MainWindow.setStyleSheet("MainWindow{border-image:url(%s/img/bg.png);}" % base_path)
        # MainWindow.setStyleSheet("MainWindow{border-image:url(D:/智源代码/高通量测序/img/bg.png);}")
        # 窗口右上角按钮
        # MainWindow.setWindowFlags(
        #     QtCore.Qt.WindowContextHelpButtonHint | QtCore.Qt.WindowCloseButtonHint)
        # MainWindow.resize(1700, 900)
        MainWindow.setMinimumSize(1700, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        # 设置控件之间的距离为0
        # self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.historyTask = QtWidgets.QGroupBox(self.centralwidget)
        self.historyTask.setStyleSheet("QGroupBox{"
                                       "font-size:23px;\n"
                                       "font-weight:700;\n"
                                       "font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;}")
        # 添加右上角按钮
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(1677215, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.help_btn = QtWidgets.QPushButton(self.frame)
        self.help_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.help_btn.setObjectName("help_btn")
        self.horizontalLayout.addWidget(self.help_btn)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.mini_btn = QtWidgets.QPushButton(self.frame)
        self.mini_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.mini_btn.setObjectName("mini_btn")
        self.horizontalLayout.addWidget(self.mini_btn)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.max_btn = QtWidgets.QPushButton(self.frame)
        self.max_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.max_btn.setObjectName("max_btn")
        self.horizontalLayout.addWidget(self.max_btn)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.close_btn = QtWidgets.QPushButton(self.frame)
        self.close_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.close_btn.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.max_btn.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.mini_btn.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.help_btn.setStyleSheet(
            '''QPushButton{background:#FFC0CB;border-radius:5px;}QPushButton:hover{background:HotPink;}''')


        self.font = QtGui.QFont()
        # self.font.setPixelSize(20)
        self.font.setPixelSize(20)
        self.historyTask.setFont(self.font)
        self.historyTask.setObjectName("historyTask")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.historyTask)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.historyTask)
        self.tableWidget_2.setFont(self.font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(0)
        # self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionsClickable(False)
        self.tableWidget_2.horizontalHeader().setStyleSheet("QHeaderView::section{background:#f5f5f5;}")
        # 表格总宽度充满表格
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 设置表格字体加粗
        font = QtGui.QFont()
        font.setPixelSize(20)
        font.setBold(True)
        font.setWeight(75)
        for i in range(9):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.tableWidget_2.setHorizontalHeaderItem(i, item)
        self.tableWidget_2.setStyleSheet('''
                    QTableWidget{
                        background:#F6F8FC;
                    }
                ''')

        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.gridLayout.addWidget(self.historyTask, 2, 1, 1, 2)
        self.typeTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.typeTree.header().setVisible(False)
        # self.typeTree.headerItem().setFont(0, font)
        self.typeTree.setMaximumSize(QtCore.QSize(350, 16777215))
        self.typeTree.setMinimumWidth(330)
        self.typeTree.setFont(self.font)
        self.typeTree.setObjectName("typeTree")
        self.typeTree.setIndentation(13)
        # self.typeTree.setLayoutDirection(Qt.RightToLeft)
        # self.typeTree.setRootIsDecorated(False)

        #新冠
        item_0 = QtWidgets.QTreeWidgetItem(self.typeTree)
        item_0.setIcon(0, QIcon(f'{base_path}/img/xinguan.png'))
        # 在新冠节点下建立子节点
        font1 = QtGui.QFont()
        font1.setPointSize(11)
        child_icon = qtawesome.icon('fa.arrow-right', color='black')
        for _ in range(2):
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1.setFont(0, font1)
            item_1.setIcon(0, child_icon)
        # Nanopore未知病原
        item_0 = QtWidgets.QTreeWidgetItem(self.typeTree)
        item_0.setIcon(0, QIcon(f'{base_path}/img/weizhi.png'))
        for i in range(3):
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1.setFont(0, font1)
            if i == 1:
                item_1.setIcon(0, qtawesome.icon('fa.bar-chart-o', color='black'))
            else:
                item_1.setIcon(0, child_icon)
        # 流感
        item_0 = QtWidgets.QTreeWidgetItem(self.typeTree)
        item_0.setIcon(0, QIcon(f'{base_path}/img/liugan.png'))
        # 病毒序列拼接（Nanopore宏基因组序列拼接）
        item_0 = QtWidgets.QTreeWidgetItem(self.typeTree)
        item_0.setIcon(0, QIcon(f'{base_path}/img/xvlie.png'))
        # 在宏基因组节点下建立子节点
        font1 = QtGui.QFont()
        font1.setPointSize(11)
        child_icon = qtawesome.icon('fa.arrow-right', color='black')
        for _ in range(3):
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            item_1.setFont(0, font1)
            item_1.setIcon(0, child_icon)

        self.typeTree.setFrameStyle(0)
        self.typeTree.setStyleSheet('''
                    QTreeWidget{
                        background:#F6F8FC;
                    }
                ''')

        self.gridLayout.addWidget(self.typeTree, 1, 0, 2, 1)
        self.newTask = QtWidgets.QGroupBox(self.centralwidget)
        self.newTask.setStyleSheet("QGroupBox{"
                                   "font-size:23px;\n"
                                   "font-weight:700;\n"
                                   "font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;}")
        self.newTask.setFont(self.font)
        self.newTask.setObjectName("newTask")
        self.newTask.setMaximumSize(1677215, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.newTask)
        self.verticalLayout.setObjectName("verticalLayout")
        addtask_icon = qtawesome.icon('fa.plus-square', color='white')
        self.addTaskbtn = QtWidgets.QPushButton(addtask_icon, '添加任务')
        self.addTaskbtn.setGeometry(QtCore.QRect(310, 330, 81, 25))
        self.addTaskbtn.setStyleSheet("QPushButton{\n"
                                      "    background:#2AC28F;\n"
                                      "    color:white;\n"
                                      "    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;\n"
                                      "    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:20px;border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{                    \n"
                                      "    background:#009933;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    border: 1px solid #3C3C3C!important;\n"
                                      "}")
        self.addTaskbtn.setMaximumSize(QtCore.QSize(200, 60))
        self.addTaskbtn.setMinimumHeight(40)
        self.addTaskbtn.setFont(self.font)
        self.addTaskbtn.setObjectName("addTaskbtn")
        self.verticalLayout.addWidget(self.addTaskbtn)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.tableWidget = QtWidgets.QTableWidget(self.newTask)
        self.tableWidget.setFont(self.font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 设置表头不可点击
        self.tableWidget.horizontalHeader().setSectionsClickable(False)
        # 设置表头背景颜色
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:#f5f5f5;}")
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)
        self.tableWidget.setStyleSheet('''
                    QTableWidget{
                        background:#F6F8FC;
                    }
                ''')
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addWidget(self.newTask, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        close_icon = qtawesome.icon('fa.times', color='white')
        self.close_btn.setIcon(close_icon)
        self.close_btn.clicked.connect(self.on_closebtn_clicked)
        max_icon = qtawesome.icon('fa.plus', color='white')
        self.max_btn.setIcon(max_icon)
        self.max_btn.clicked.connect(self.on_maxbtn_clicked)
        mini_icon = qtawesome.icon('fa.minus', color='white')
        self.mini_btn.setIcon(mini_icon)
        self.mini_btn.clicked.connect(self.on_minibtn_clicked)
        help_icon = qtawesome.icon('fa.question', color='white')
        self.help_btn.setIcon(help_icon)
        self.help_btn.clicked.connect(self.on_helpbtn_clicked)
        MainWindow.setWindowTitle(self._translate("MainWindow", "高通量测序分析（完整版）"))
        self.historyTask.setTitle(self._translate("MainWindow", "历史任务"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(self._translate("MainWindow", "任务名称"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(self._translate("MainWindow", "任务类型"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(self._translate("MainWindow", "样品名称"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(self._translate("MainWindow", "Barcode"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(self._translate("MainWindow", "起始时间"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(self._translate("MainWindow", "结束时间"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(self._translate("MainWindow", "任务状态"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(self._translate("MainWindow", "结果展示"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(self._translate("MainWindow", "操作"))
        self.typeTree.headerItem().setText(0, self._translate("MainWindow", "任务类型"))
        __sortingEnabled = self.typeTree.isSortingEnabled()
        self.typeTree.setSortingEnabled(False)
        self.typeTree.topLevelItem(0).setText(0, self._translate("MainWindow", "Nanopore新冠病毒"))
        self.typeTree.topLevelItem(0).child(0).setText(0, self._translate("MainWindow", "序列拼接"))
        self.typeTree.topLevelItem(0).child(1).setText(0, self._translate("MainWindow", "溯源与分子进化树"))
        self.typeTree.topLevelItem(1).setText(0, self._translate("MainWindow", "Nanopore未知病原"))
        self.typeTree.topLevelItem(1).child(0).setText(0, self._translate("MainWindow", "序列分类"))
        self.typeTree.topLevelItem(1).child(1).setText(0, self._translate("MainWindow", "可视化分析"))
        self.typeTree.topLevelItem(1).child(2).setText(0, self._translate("MainWindow", "序列提取"))
        self.typeTree.topLevelItem(2).setText(0, self._translate("MainWindow", "Nanopore流感病毒拼接"))
        self.typeTree.topLevelItem(3).setText(0, self._translate("MainWindow", "Nanopore宏基因组序列拼接"))
        self.typeTree.topLevelItem(3).child(0).setText(0, self._translate("MainWindow", "查找参考序列"))
        self.typeTree.topLevelItem(3).child(1).setText(0, self._translate("MainWindow", "序列拼接"))
        self.typeTree.topLevelItem(3).child(2).setText(0, self._translate("MainWindow", "从头拼接"))
        # self.typeTree.topLevelItem(6).setText(0, self._translate("MainWindow", "序列比对"))
        # self.typeTree.topLevelItem(6).child(0).setText(0, self._translate("MainWindow", "核酸BLAST"))
        self.typeTree.setSortingEnabled(__sortingEnabled)
        self.typeTree.itemClicked.connect(self.tree_click)
        self.typeTree.itemClicked.connect(self.refresh_table)
        # 设置默认选中第一个树节点，创建任务时可直接创建
        self.typeTree.setCurrentItem(self.typeTree.topLevelItem(0))
        # 设置树节点背景颜色
        # brush_red = QBrush(Qt.lightGray)
        # self.typeTree.topLevelItem(0).setBackground(0, brush_red)
        self.newTask.setTitle(self._translate("MainWindow", "任务管理"))
        self.addTaskbtn.setText(self._translate("MainWindow", "新建任务"))
        # 按钮隐藏
        # op = QtWidgets.QGraphicsOpacityEffect()
        # # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        # op.setOpacity(0)
        # self.addTaskbtn.setGraphicsEffect(op)

        self.addTaskbtn.clicked.connect(self.add_param)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(self._translate("MainWindow", "任务名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(self._translate("MainWindow", "任务类型"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(self._translate("MainWindow", "开始时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(self._translate("MainWindow", "持续时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(self._translate("MainWindow", "运行状态"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(self._translate("MainWindow", "中间文件"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(self._translate("MainWindow", "操作"))

    def add_param(self):
        """
        点击添加参数弹出子窗口
        :return:
        """
        current_tree = self.typeTree.currentItem().text(0)
        s_sql = """select taskStatus from task"""
        # result = self.cursor.execute(s_sql)
        data = self.cursor.execute(s_sql).fetchall()
        result = ''.join([*map(lambda x: ''.join(x[0]), data)])
        # 2021-08-15 10:27:43
        # 取消每次只能运行一个任务的限制
        # if '正在运行' not in result:
        child_win = QDialog()
        # 参数添加窗口默认为诺如窗口，即只添加路径参数
        child_ui = ''
        if current_tree in ['Nanopore流感病毒拼接']:
            child_ui = Liugan_UI()
        elif current_tree == '溯源与分子进化树':
            child_ui = Xvlie_UI()
        elif current_tree == '序列提取':
            child_ui = Xvlietiqu_UI()
        elif current_tree in ['查找参考序列']:
            child_ui = Czckxl_UI()
        elif current_tree == '序列拼接':
            if self.typeTree.currentItem().parent().text(0) == 'Nanopore新冠病毒':
                try:
                    con_model = config.get('Metagenome', 'model_list')
                    model_list = con_model.split(',')
                    pri_model = config.get('Metagenome', 'primmer_list')
                    primmer_list = pri_model.split(',')
                except:
                    QMessageBox.warning(self.centralwidget, '警告', '配置文件中模型列表参数有误！', QMessageBox.Ok)
                else:
                    child_ui = Xinguan_Ui(model_list, primmer_list)
            else:
                child_ui = Xlpj_UI()
        elif current_tree == '序列拼接(基于参考序列)':
            child_ui = Erxlpj_UI()
        elif current_tree == '数据质控' or current_tree == '二代测序':
            child_ui = Zhikong_UI()
        elif current_tree == '序列分类':
            child_ui = WZxlfl_UI()
        elif current_tree == '从头拼接':
            if self.typeTree.currentItem().parent().text(0) == 'Nanopore宏基因组序列拼接':
                try:
                    con_model = config.get('Metagenome', 'model_list')
                    model_list = con_model.split(',')
                except:
                    QMessageBox.warning(self.centralwidget, '警告', '配置文件中模型列表参数有误！', QMessageBox.Ok)
                else:
                    child_ui = HJYctpj_UI(model_list)
            elif self.typeTree.currentItem().parent().text(0) == '二代测序':
                child_ui = EDctpj_UI()
        else:
            QMessageBox.warning(self.centralwidget, '警告', '请选择具体的功能节点', QMessageBox.Ok)
        if child_ui:
            child_ui.setupUi(child_win)
            window_name = self.typeTree.currentItem().text(0)
            # 首先判断当前的节点是否有父节点，如有则拼接在当前节点之前
            # 子窗口名称即为程序运行参数中的任务类型
            if self.typeTree.currentItem().parent():
                window_name = self.typeTree.currentItem().parent().text(0) + '-' + self.typeTree.currentItem().text(0)
            child_ui.Dialog.setWindowTitle(self._translate('Dialog', window_name))
            child_ui.Dialog.setWindowIcon(self.typeTree.currentItem().icon(0))
            # 接收子窗口的参数，前提是子窗口发送信号给主窗口，否则报错
            child_ui.paramSignal.connect(self.print_params)
            # 接收开始运行命令的信号，通过子界面的运行按钮来发送信号
            child_ui.startSignal.connect(self.run_)
            child_win.exec_()
        # else:
        #     QMessageBox.warning(self.centralwidget, "警告", '有任务正在运行中...', QMessageBox.Ok)

    def print_params(self, params):
        """
        接收参数窗口传递的参数字典，方便与传递给命令程序
        :param params: 参数窗口提交的参数字典
        :return:
        """
        # print(f'子窗口的参数为{params}')
        self.params = params
        item = self.typeTree.currentItem()
        self.refresh_table(item)

    def run_(self, signal):
        """
        参数窗口提交参数后开始运行程序
        :param signal: 提交参数成功的信号
        :return:
        """
        if signal == 1:
            # print(f'开始运行程序，参数为{data}')
            # 运行程序
            if self.typeTree.currentItem().text(0) == '序列拼接':
                if self.typeTree.currentItem().parent().text(0) == 'Nanopore新冠病毒':
                    # 2021-12-25 04:28:36 修改新冠序列拼接运行python文件
                    self.do_pyfile(self.params)
                else:
                    self.do_hongjiyin(self.params)
            elif self.typeTree.currentItem().text(0) == '溯源与分子进化树':
                self.do_pyfile(self.params)
            elif self.typeTree.currentItem().text(0) == '诺如病毒':
                file_name = config.get('Norovirus', 'file_name')
                self.do_snakemake(self.params, file_name, self.nuoru_file_list)
            elif self.typeTree.currentItem().text(0) == '序列提取':
                self.do_xvlietiqu(self.params)
            elif self.typeTree.currentItem().text(0) == 'Nanopore流感病毒拼接':
                self.do_liugan(self.params)
            elif self.typeTree.currentItem().text(0) in ['查找参考序列']:
                self.do_hongjiyin(self.params)
            elif self.typeTree.currentItem().text(0) in ['数据质控', '二代测序']:
                self.do_datacontrol(self.params)
            elif self.typeTree.currentItem().text(0) == '序列拼接(基于参考序列)':
                self.do_erdaixlpj(self.params)
            elif self.typeTree.currentItem().text(0) in ['序列分类', '从头拼接']:
                self.do_pyfile(self.params)
            start_ = QDateTime.currentDateTime()
            self.start_time = start_.toString('yyyy-MM-dd hh:mm:ss')
            # 设置时间间隔并启动定时器
            self.timer.start(1000)

    def judge_start(self, data, fir_name):
        """
        新冠测序，根据已存在的文件夹判断起始步骤，若都存在在手动输入起始步骤
        :param data:
        :param fir_name:
        :return:
        """
        file_path = data['file_path']
        dir_list = os.listdir(file_path)
        ori_sec_name = config.get('SARS-COV-2', 'thi_name')
        flag = 0
        if fir_name in dir_list and ori_sec_name not in dir_list:
            flag = 1
        elif ori_sec_name in dir_list and fir_name not in dir_list:
            flag = 3
        elif ori_sec_name in dir_list and fir_name in dir_list:
            messageBox = QMessageBox()
            messageBox.setWindowTitle('提示')
            messageBox.setText('请确认起始步骤：')
            messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            buttonY = messageBox.button(QMessageBox.Yes)
            buttonY.setText('1')
            buttonN = messageBox.button(QMessageBox.No)
            buttonN.setText('3')
            messageBox.exec_()
            if messageBox.clickedButton() == buttonY:
                flag = 1
            elif messageBox.clickedButton() == buttonN:
                flag = 3
            else:
                self.status = '运行失败！'
                QMessageBox.information(self.centralwidget, '提示', '程序已停止运行', QMessageBox.Ok)
        else:
            self.status = '运行失败！'
            QMessageBox.warning(self.centralwidget, '警告', '运行失败：缺失起始文件夹！', QMessageBox.Ok)
        return flag

    def do_xinguan(self, data):
        """
        执行代码程序(新冠)
        :param data: 执行程序所需要的参数
        :return:
        """
        a = RunPythonFile(data)
        d_sql = """delete from task where taskNm=? and taskType=?"""
        d_p_sql = """delete from params where taskNm=? and taskType=?"""
        self.cursor.execute(d_sql, (data['task_name'], data['task_type']))
        self.cursor.execute(d_p_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        a.exitSignal.connect(self.output)
        self.thread1 = threading.Thread(target=a.run, name='main')
        self.thread1.start()
        i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
        self.cursor.execute(i_sql,
                            (data['task_name'], data['task_type'], ','.join(data['sample_list']),
                             ','.join(data['barcode_list']),
                             data['result_path']))
        self.conn.commit()

    def judge_path(self, file_path):
        """
        判断起始文件夹是否有效
        :param file_path:
        :return:
        """
        flag = 0
        result = ''
        if os.path.exists(file_path):
            dir_list = os.listdir(file_path)
            dir_data = ''.join(dir_list)
            try:
                if self.typeTree.currentItem().text(0) == '诺如病毒':
                    result = re.findall(r'0\.rawdata', dir_data)
                elif self.typeTree.currentItem().text(0) in ['Nanopore未知病原', 'Nanopore流感病毒拼接', 'Nanopore宏基因组序列拼接']:
                    result = re.findall(r'barcode\d+', dir_data)
            except Exception as e:
                QMessageBox.warning(self.centralwidget, '警告', f'运行失败：起始文件夹判断失败,{e}！！！', QMessageBox.Ok)
        if result:
            flag = 1
        else:
            QMessageBox.warning(self.centralwidget, '警告', '运行失败：起始文件夹存在错误！！！', QMessageBox.Ok)
        return flag

    def do_snakemake(self, data, file_name, file_list):
        """
        执行snakemake程序文件
        :param data: 程序运行参数
        :param file_name: snakemake文件名称
        :param file_list: 结果文件列表
        :return:
        """
        flag = 0
        a = RunSnakemake(data, file_name)
        work_file = data['work_file']
        task_name = data['task_name']
        s_sql = """select * from task where taskNm = ? and taskType=?"""
        result = self.cursor.execute(s_sql, (task_name, data['task_type']))
        task_data = result.fetchall()
        if not os.path.exists(work_file):
            QMessageBox.warning(self.centralwidget, '警告', f'{work_file}：该路径不存在！', QMessageBox.Yes)
        elif len(task_data) > 0 or set(file_list).issubset(set(os.listdir(work_file))):
            reply = QMessageBox.warning(self.centralwidget, '警告', '当前任务已存在，是否删除？', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    for file in file_list:
                        if os.path.exists(work_file + '/' + file):
                            shutil.rmtree(work_file + '/' + file)
                    d_sql = """delete from task where taskNm=? and taskType=?"""
                    d_p_sql = """delete from params where taskNm=? and taskType=?"""
                    self.cursor.execute(d_sql, (task_name, data['task_type']))
                    self.conn.commit()
                    self.cursor.execute(d_p_sql, (task_name, data['task_type']))
                    self.conn.commit()
                except Exception as e:
                    logger.error(f'数据库删除失败：{str(e)}')
                finally:
                    flag = self.judge_path(a.path)
            elif reply == QMessageBox.No:
                self.status = '停止运行'
                QMessageBox.information(self.centralwidget, '提示', '程序已停止运行', QMessageBox.Ok)
        else:
            flag = self.judge_path(a.path)
        if flag == 1:
            a.exitSignal.connect(self.output)
            # a.changeStatus.connect(self.refresh_table)
            self.thread1 = threading.Thread(target=a.run, name='main')
            self.thread1.start()
            i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
            self.cursor.execute(i_sql,
                                (data['task_name'], data['task_type'], ','.join(data['sample_list']), ','.join(data['barcode_list']),
                                 data['file_path']))
            self.conn.commit()

    def judge_status(self, a, work_file, task_name):
        """
        检查当前任务名是否已经存在(数据库以及本地文件夹)
        :param a: 运行命令类的实例
        :param work_file: 结果文件存放路径
        :param task_name: 任务名称
        :return:
        """
        flag = 0
        s_sql = """select * from task where taskNm = ? and taskType=?"""
        result = self.cursor.execute(s_sql, (task_name, a.task_type))
        task_data = result.fetchall()
        if os.path.exists(work_file) and (task_name in os.listdir(work_file) or len(task_data) > 0):
            reply = QMessageBox.warning(self.centralwidget, '警告', '当前任务已存在，是否删除？', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    if os.path.exists(work_file + '/' + task_name):
                        shutil.rmtree(work_file + '/' + task_name)
                    d_sql = """delete from task where taskNm=? and taskType=?"""
                    d_p_sql = """delete from params where taskNm=? and taskType=?"""
                    self.cursor.execute(d_sql, (task_name, a.task_type))
                    self.conn.commit()
                    self.cursor.execute(d_p_sql, (task_name, a.task_type))
                    self.conn.commit()
                except Exception as e:
                    logger.error(f'数据库删除失败：{str(e)}')
                finally:
                    flag = self.judge_path(a.path)
            elif reply == QMessageBox.No:
                self.status = '停止运行'
                QMessageBox.information(self.centralwidget, '提示', '程序已停止运行', QMessageBox.Ok)
        elif os.path.exists(work_file) and task_name not in os.listdir(work_file):
            flag = self.judge_path(a.path)
        else:
            QMessageBox.warning(self.centralwidget, '警告', f'{work_file}： 该路径不存在！', QMessageBox.Ok)
        return flag

    def do_weizhi(self, data):
        """
        执行代码程序（weizhi）
        :param data: 执行程序所需要的参数
        :return:
        """
        a = RunWeizhi(data)
        work_file = data['work_file']
        task_name = data['task_name']
        flag = self.judge_status(a, work_file, task_name)
        if flag == 1:
            a.exitSignal.connect(self.output)
            self.thread1 = threading.Thread(target=a.run, name='main')
            self.thread1.start()
            i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
            self.cursor.execute(i_sql,
                                (data['task_name'], data['task_type'], ','.join(data['sample_list']), ','.join(data['barcode_list']),
                                 data['work_file']))
            self.conn.commit()

    def do_liugan(self, data):
        """
        执行流感一系列代码程序
        :param data: 执行程序所需要的参数
        :return:
        """
        a = RunLiugan(data)
        d_sql = """delete from task where taskNm=? and taskType=?"""
        d_p_sql = """delete from params where taskNm=? and taskType=?"""
        self.cursor.execute(d_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        self.cursor.execute(d_p_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        a.exitSignal.connect(self.output)
        self.thread1 = threading.Thread(target=a.run, name='main')
        self.thread1.start()
        i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
        self.cursor.execute(i_sql,
                            (data['task_name'], data['task_type'], ','.join(data['sample_list']), ','.join(data['barcode_list']),
                             data['work_file']))
        self.conn.commit()

    def do_hongjiyin(self, data):
        """
        执行宏基因组一系列代码程序
        :param data: 执行程序所需要的参数
        :return:
        """
        a = RunHongjiyin(data)
        d_sql = """delete from task where taskNm=? and taskType=?"""
        d_p_sql = """delete from params where taskNm=? and taskType=?"""
        self.cursor.execute(d_sql, (data['task_name'], data['task_type']))
        self.cursor.execute(d_p_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        a.exitSignal.connect(self.output)
        self.thread1 = threading.Thread(target=a.run, name='main')
        self.thread1.start()
        i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
        self.cursor.execute(i_sql,
                            (data['task_name'], data['task_type'], ','.join(data['sample_list']), ','.join(data['barcode_list']),
                             data['work_file']))
        self.conn.commit()

    def do_xvlietiqu(self, data):
        """
        执行未知病原相关python脚本
        :param : 运行脚本的相关参数
        :return:
        """
        a = RunPython(data)
        d_sql = """delete from task where taskNm=? and taskType=?"""
        d_p_sql = """delete from params where taskNm=? and taskType=?"""
        self.cursor.execute(d_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        self.cursor.execute(d_p_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        a.exitSignal.connect(self.output)
        self.thread1 = threading.Thread(target=a.run, name='main')
        self.thread1.start()
        i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
        self.cursor.execute(i_sql,
                            (data['task_name'], data['task_type'], ','.join(data['sample_list']), ','.join(data['barcode_list']),
                             data['work_file']))
        self.conn.commit()

    def do_datacontrol(self, data):
        """
        执行二代测序-数据质控相关命令
        :param data: 执行程序所需要的参数
        :return:
        """
        a = RunDataControl(data)
        d_sql = """delete from task where taskNm=? and taskType=?"""
        d_p_sql = """delete from params where taskNm=? and taskType=?"""
        self.cursor.execute(d_sql, (data['task_name'], data['task_type']))
        self.cursor.execute(d_p_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        a.exitSignal.connect(self.output)
        self.thread1 = threading.Thread(target=a.run, name='main')
        self.thread1.start()
        i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
        self.cursor.execute(i_sql,
                            (data['task_name'], data['task_type'], ','.join(data['sample_list']), ','.join(data['barcode_list']),
                             data['work_file']))
        self.conn.commit()

    def do_erdaixlpj(self, data):
        """
        执行二代测序-序列拼接(基于参考序列)相关命令
        :param data: 执行程序所需要的参数
        :return:
        """
        a = RunErdaixlpj(data)
        d_sql = """delete from task where taskNm=? and taskType=?"""
        d_p_sql = """delete from params where taskNm=? and taskType=?"""
        self.cursor.execute(d_sql, (data['task_name'], data['task_type']))
        self.cursor.execute(d_p_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        a.exitSignal.connect(self.output)
        self.thread1 = threading.Thread(target=a.run, name='main')
        self.thread1.start()
        i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
        self.cursor.execute(i_sql,
                            (data['task_name'], data['task_type'], ','.join(data['sample_list']), ','.join(data['barcode_list']),
                             data['work_file']))
        self.conn.commit()

    def do_pyfile(self, data):
        """
        执行python文件
        :param data: 执行程序所需要的参数
        :return:
        """
        a = RunPythonFile(data)
        d_sql = """delete from task where taskNm=? and taskType=?"""
        d_p_sql = """delete from params where taskNm=? and taskType=?"""
        self.cursor.execute(d_sql, (data['task_name'], data['task_type']))
        self.cursor.execute(d_p_sql, (data['task_name'], data['task_type']))
        self.conn.commit()
        a.exitSignal.connect(self.output)
        self.thread1 = threading.Thread(target=a.run, name='main')
        self.thread1.start()
        i_sql = """insert into params(taskNm, taskType, sampleNm, barcode, filepath)values (?,?,?,?,?)"""
        self.cursor.execute(i_sql,
                            (data['task_name'], data['task_type'], ','.join(data['sample_list']), ','.join(data['barcode_list']),
                             data['result_path']))
        self.conn.commit()

    def output(self, msg):
        """
        接收程序中发送的运行状态信号
        :param msg: 发送的信号：self.status
        :return:
        """
        self.refresh_table(self.typeTree.currentItem())
        self.status = msg
        reply = ''
        # if self.status not in ['运行中...', '已完成']:
        result = re.findall(r'开始|完成|正在', self.status)
        if not result:
            self.timer.stop()
            reply = QMessageBox.warning(self.centralwidget, '警告', self.status, QMessageBox.Ok)
        elif self.status == '已完成':
            self.timer.stop()
            reply = QMessageBox.information(self.centralwidget, '提示', '任务已完成！', QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            self.refresh_table(self.typeTree.currentItem())
        # print(f'信号为:{msg}')

    def tree_click(self, item):
        """
        判断当前节点为未知病原-可视化分析时
        调用R程序来打开网页
        :param item:
        :return:
        """
        parent_ = ''
        if item.parent():
            parent_ = item.parent().text(0)
        if parent_ == 'Nanopore未知病原' and item.text(0) == '可视化分析':
            data = {
                'task_type': '',
                'task_name': '',
                'sample_list': '',
                'barcode_list': '',
                'file_path': '',
                'work_file': ''}
            r_ = RunWeizhi(data)
            r_.run_R()
            a = WebShow()
            a.open_weizhi()

    def get_db_data(self, tType):
        """
        获取数据库中的所有数据
        根据任务状态区分正在运行的任务、已结束的任务
        :type tType: 任务类型
        :return:
        """
        # print(f'当前任务类型为{tType}')
        s_sql = "select * from task where taskType like '" + tType + "%' order by startTime desc"
        result = self.cursor.execute(s_sql)
        task_data = result.fetchall()
        new_task_list = []
        history_task = []
        for task in task_data:
            # if '运行' in task[-2]:
            if re.findall(r'正在', task[-2]):
                new_task_list.append(task)
            else:
                history_task.append(task)
        history_task_list = []
        for his_data in history_task:
            task_name = his_data[1]
            # s_sql = """select sampleNm, barcode from params where taskNm=""" + task_name + """ and taskType like '""" + tType + "%'"
            s_sql = f"select sampleNm, barcode from params where taskNm='{task_name}' and taskType like '{tType}%'"
            result = self.cursor.execute(s_sql)
            data = result.fetchone() if result else ('', '')
            sample_list = data[0]
            barcode_list = data[1]
            his_data = his_data + (sample_list, barcode_list)
            history_task_list.append(his_data)

        return new_task_list, history_task_list

    def refresh_table(self, item):
        """
        点击树节点，刷新页面中的表格数据
        :param item:
        :return:
        """
        # print(f'刷新表格：{item.text(0)}')    # 树节点名称
        task_type = item.text(0)
        if item.parent():
            if task_type == '可视化分析':
                task_type = 'Nanopore未知病原'
            else:
                task_type = item.parent().text(0) + '-' + item.text(0)
        new_task_list, history_task_list = self.get_db_data(task_type)
        # 新建任务
        self.tableWidget.setRowCount(len(new_task_list))
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.DoubleClicked)
        self.tableWidget.verticalHeader().setVisible(False)
        # 禁止表格数据自动换行，影响表格整体样式
        self.tableWidget.setWordWrap(False)
        for row, task_list in enumerate(new_task_list):
            # 获取系统当前时间
            time = QDateTime.currentDateTime()
            # 设置系统时间的显示格式
            timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss')
            delta = self.get_period(task_list[3], timeDisplay)
            table_data_new = [task_list[1], task_list[2], task_list[3], delta, task_list[6]]
            for col, new_task in enumerate(table_data_new):
                table_item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(row, col, table_item)
                table_item = self.tableWidget.item(row, col)
                table_item.setText(self._translate("MainWindow", new_task))
                table_item.setTextAlignment(Qt.AlignHCenter)
            # 添加删除按钮
            del_icon = qtawesome.icon('fa.trash-o', color='white')
            del_btn = QtWidgets.QPushButton('删除')
            del_btn.setStyleSheet('''
                    QPushButton{
                        border:none;
                        color:white;
                        height:40px;
                        padding-left:10px;
                        padding-right:10px;
                        text-align:center;
                        background:#FF6666;
                        margin:2% 20% 2% 20%;
                        border-radius: 5px;
                    }
                    QPushButton:hover{
                        border:1px solid #F3F3F5;
                        border-radius:5px;
                        background:#FF0033;
                    }
                ''')
            del_btn.setFont(self.font)
            # btn.setMaximumSize(QtCore.QSize(120, 40))
            del_btn.clicked.connect(partial(self.del_data, self.tableWidget))
            self.tableWidget.setCellWidget(row, len(table_data_new) + 1, del_btn)
            # 添加打开文件夹按钮
            open_icon = qtawesome.icon('fa.folder-open', color="white")
            open_btn = QtWidgets.QPushButton('打开文件')
            open_btn.setFont(self.font)
            # btn.setMaximumSize(QtCore.QSize(120, 40))
            open_btn.setStyleSheet('''
                        QPushButton{
                            border:none;
                            color:white;
                            height:40px;
                            padding-left:10px;
                            padding-right:10px;
                            text-align:center;
                            background:#0099CC;
                            margin:2% 20% 2% 20%;
                            border-radius: 5px;
                        }
                        QPushButton:hover{
                            border:1px solid #F3F3F5;
                            border-radius:5px;
                            background:#0066CC;
                        }
                    ''')
            open_btn.clicked.connect(partial(self.open_file, self.tableWidget))
            self.tableWidget.setCellWidget(row, len(table_data_new), open_btn)

        # 历史任务
        self.tableWidget_2.setRowCount(len(history_task_list))
        # self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置表格双击可编辑（为了显示省略内容）
        self.tableWidget_2.setEditTriggers(QtWidgets.QTableWidget.DoubleClicked)
        # 设置表格行自动变色
        self.tableWidget_2.setAlternatingRowColors(True)
        # 垂直表格头隐藏
        self.tableWidget_2.verticalHeader().setVisible(False)
        # 禁止表格数据自动换行，影响表格整体样式
        self.tableWidget_2.setWordWrap(False)
        for row, history_list in enumerate(history_task_list):
            # table_data_old = [history_list[1], history_list[2], history_list[3], history_list[4], history_list[6]]
            table_data_old = [history_list[1], history_list[2], history_list[8], history_list[9], history_list[3], history_list[4], history_list[6]]
            for col, old_task in enumerate(table_data_old):
                table_item1 = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setItem(row, col, table_item1)
                table_item1 = self.tableWidget_2.item(row, col)
                table_item1.setText(self._translate("MainWindow", old_task))
                table_item1.setTextAlignment(Qt.AlignHCenter)
                table_item1.setToolTip(old_task)
                QToolTip.setFont(self.font)
                if old_task and old_task.find('失败') > -1:
                    brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                    brush.setStyle(QtCore.Qt.NoBrush)
                    table_item1.setForeground(brush)
            # 添加删除按钮
            del_btn1 = QtWidgets.QPushButton('删除')
            del_btn1.setStyleSheet('''
                    QPushButton{
                        border:none;
                        color:white;
                        height:40px;
                        padding-left:10px;
                        padding-right:10px;
                        text-align:center;
                        background:#FF6666;
                        margin:2% 20% 2% 20%;
                        border-radius: 5px;
                    }
                    QPushButton:hover{
                        border:1px solid #F3F3F5;
                        border-radius:5px;
                        background:#FF0033;
                    }
                ''')
            del_btn1.setFont(self.font)
            del_btn1.clicked.connect(partial(self.del_data, self.tableWidget_2))
            self.tableWidget_2.setCellWidget(row, len(table_data_old) + 1, del_btn1)
            if history_list[-2] and history_list[-2].find('失败') > -1:
                table_item1 = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setItem(row, len(table_data_old), table_item1)
                table_item1 = self.tableWidget_2.item(row, len(table_data_old))
                table_item1.setText(self._translate("MainWindow", history_list[-1]))
                table_item1.setTextAlignment(Qt.AlignHCenter)
            else:
                open_btn1 = QtWidgets.QPushButton('打开文件')
                open_btn1.setStyleSheet('''
                        QPushButton{
                            border:none;
                            color:white;
                            height:40px;
                            padding-left:10px;
                            padding-right:10px;
                            text-align:center;
                            background:#0099CC;
                            margin:2% 20% 2% 20%;
                            border-radius: 5px;
                        }
                        QPushButton:hover{
                            border:1px solid #F3F3F5;
                            border-radius:5px;
                            background:#0066CC;
                        }
                    ''')
                open_btn1.setFont(self.font)
                open_btn1.clicked.connect(partial(self.open_file, self.tableWidget_2))
                self.tableWidget_2.setCellWidget(row, len(table_data_old), open_btn1)
        # 根据指定内容定位到表格行数
        # item_nm = self.tableWidget_2.findItems('444', Qt.MatchExactly)[0]
        # item_tp = self.tableWidget_2.findItems('二代测序-序列拼接(基于参考序列)', Qt.MatchExactly)[0]
        # print(item_nm.row(), item_tp.row())

    def del_data(self, table):
        """
        点击按钮删除表格的当前行，并删除本地结果文件夹
        :return:
        """
        button = self.sender()
        flag = 0    # 历史任务删除数据的标志
        reply = None   # 新建任务的删除标志
        # task_name = ''
        if button:
            row = table.indexAt(button.pos()).row()
            task_name = table.item(row, 0).text()
            task_type = table.item(row, 1).text()
            # 删除本地文件夹
            if table == self.tableWidget_2:
                flag = 1
                s_sql = """select filepath from params where taskNm=? and taskType=?"""
                result = self.cursor.execute(s_sql, (task_name, task_type))
                path = result.fetchone()
                path = path[0] if path else '.'
                work_file = path + '/' + task_name
                result_file_list = []
                if self.typeTree.currentItem().text(0) == '诺如病毒':
                    result_file_list = self.nuoru_file_list
                for file in result_file_list:
                    if os.path.exists(path + '/' + file):
                        shutil.rmtree(path + '/' + file)
                if os.path.exists(work_file):
                    shutil.rmtree(work_file)
            if table == self.tableWidget:
                content = '任务正在运行中，删除后当前命令仍将继续\n在后台运行，是否删除？'
                reply = QtWidgets.QMessageBox.question(self.centralwidget,
                                                       '删除任务',
                                                       content,
                                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                       QtWidgets.QMessageBox.No)
            if reply == QMessageBox.Yes or flag:
                    # quit()
                # 删除数据库数据
                d_sql = """delete from task where taskNm=? and taskType=?"""
                d_p_sql = """delete from params where taskNm=? and taskType=?"""
                self.cursor.execute(d_sql, (task_name, task_type))
                self.conn.commit()
                self.cursor.execute(d_p_sql, (task_name, task_type))
                self.conn.commit()
                table.removeRow(row)

    def open_file(self, table):
        """
        根据当前任务名打开结果文件
        :return:
        """
        button = self.sender()
        xinguan_result = config.get('SARS-COV-2', 'for_name')
        if button:
            row = table.indexAt(button.pos()).row()
            task_name = table.item(row, 0).text()  # 任务名称
            task_type = table.item(row, 1).text()  # 任务类型
            status = table.item(row, 4).text()     # 任务状态
            s_sql = """select filepath from params where taskNm=? and taskType=?"""
            result = self.cursor.execute(s_sql, (task_name, task_type))
            path = result.fetchone()
            path = path[0] if path else '.'
            # work_file = path
            if '正在运行' in status or task_type not in ['Nanopore新冠病毒', 'Nanopore新冠病毒-序列拼接']:
                work_file = path
            else:
                work_file = path + '/' + task_name + f"/{xinguan_result}"
            print(f'打开文件参数如下：{task_name, task_type, work_file}')
            if os.path.exists(work_file):
                if '正在运行' in status:
                    QFileDialog.getOpenFileNames(self.MainWindow, "选取文件夹", work_file)
                else:
                    file_type = ''
                    if task_type in ['Nanopore新冠病毒', 'Nanopore新冠病毒-序列拼接']:
                        file_type = 'fasta(*.consensus.fasta);;bam(*.primertrimmed.rg.sorted.bam);;ALL(*)'
                    directory1 = QFileDialog.getOpenFileNames(self.MainWindow, "选取文件夹", work_file, file_type)
                    if directory1[1] == 'fasta(*.consensus.fasta)':
                        if directory1[0]:
                            logger.info(f'{"*" * 20}当前任务名称为{task_name}\n当前打开的文件为{directory1[0]}')
                            try:
                                a = WebShow()
                                a.get_result(directory1[0])
                            except Exception as e:
                                logger.error(f'打开网页失败{e}')
                                QMessageBox.warning(self.centralwidget, '警告', '打开网页失败！', QMessageBox.Ok)
                    elif directory1[1] == 'bam(*.primertrimmed.rg.sorted.bam)':
                        # 展示折线图和表格
                        # try:
                        w = QDialog()
                        w_ui = QtDraw()
                        w_ui.path_list = directory1[0]
                        w_ui.init_ui(w)
                        w.exec_()

            else:
                QMessageBox.warning(self.centralwidget, "警告", '本地文件夹不存在', QMessageBox.Ok)

    def showTime(self):
        """
        定义一个计时器，目前是写死的状态，即固定是在新建任务的第一行第四列
        :return:
        """
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss')
        delta = self.get_period(self.start_time, timeDisplay)
        row_num = self.tableWidget.rowCount()
        if row_num == 1:
            table_item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(0, 3, table_item)
            table_item = self.tableWidget.item(0, 3)
            table_item.setText(self._translate("MainWindow", delta))
            table_item.setTextAlignment(Qt.AlignHCenter)
            return delta

    def get_period(self, s_time, e_time):
        """
        计算时间间隔
        :param s_time: 开始时间
        :param e_time: 结束时间
        :return:
        """
        db_time = datetime.strptime(s_time, '%Y-%m-%d %H:%M:%S') if s_time else datetime.now()
        end_time = datetime.strptime(e_time, '%Y-%m-%d %H:%M:%S') if e_time else datetime.now()
        delta = end_time - db_time
        delta = str(delta).split('.')[0] if delta else '00:00:00'
        return delta

    @pyqtSlot()
    def on_closebtn_clicked(self):
        """
        关闭窗口
        """
        self.MainWindow.close()

    @pyqtSlot()
    def on_minibtn_clicked(self):
        """
        最小化窗口
        """
        self.MainWindow.showMinimized()

    @pyqtSlot()
    def on_maxbtn_clicked(self):
        """
        最大化窗口
        :return:
        """
        # print(self.MainWindow.isMaximized())
        if not self.MainWindow.isMaximized():
            self.MainWindow.showMaximized()
        else:
            self.MainWindow.showNormal()

        # self.MainWindow.showNormal()

    @pyqtSlot()
    def on_helpbtn_clicked(self):
        content = """Current version: 1.12  """
        messageBox = QMessageBox()
        messageBox.setWindowIcon(QIcon(f'{base_path}/img/logo.png'))
        messageBox.setWindowTitle('高通量测序')
        messageBox.setText(content)
        messageBox.setStandardButtons(QMessageBox.Yes)
        buttonY = messageBox.button(QMessageBox.Yes)
        buttonY.setText('Ok')
        messageBox.exec_()



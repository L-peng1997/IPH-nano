# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 19:04
# @Author  : Lvp
# @File    : drawZhex.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import pandas as pd
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtCore, QtGui
import os

# 项目路径
base_path = os.getcwd().replace('\\', '/')


class QtDraw(object):

    def __init__(self):
        super(QtDraw, self).__init__()
        self.path_list = []

    def init_ui(self, Dialog):
        Dialog.resize(1050, 800)
        Dialog.setObjectName('PyQt5 Draw')
        Dialog.setWindowIcon(QIcon(f'{base_path}/img/logo.png'))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("centralwidget")
        self.font = QtGui.QFont()
        self.font.setPointSize(12)

        # TODO:这里是结合的关键
        self.fig = plt.Figure(figsize=(10, 10.5))
        self.canvas = FC(self.fig)
        self.slot_btn_start()
        self.scroll = QtWidgets.QScrollArea(Dialog)
        self.scroll.setWidget(self.canvas)
        self.nav = NavigationToolbar(self.canvas, Dialog)
        self.n_table = QtWidgets.QTableWidget()
        self.n_table.setFixedSize(16777215, 200)
        self.n_table.setColumnCount(3)
        self.n_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 设置表格双击可编辑（为了显示省略内容）
        self.n_table.setEditTriggers(QtWidgets.QTableWidget.DoubleClicked)
        # 设置表格行自动变色
        self.n_table.setAlternatingRowColors(True)
        # 垂直表格头隐藏
        self.n_table.verticalHeader().setVisible(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.n_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.n_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.n_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.n_table.setHorizontalHeaderItem(2, item)

        # widget = QWidget()
        # layout = QVBoxLayout()
        self.verticalLayout.addWidget(self.nav)
        self.verticalLayout.addWidget(self.scroll)
        self.verticalLayout.addWidget(self.n_table)
        # widget.setLayout(layout)
        self.retranslateUi(Dialog)
        self.add_table()

    def retranslateUi(self, Dialog):
        self._translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(self._translate("Dialog", "分析结果"))
        item = self.n_table.horizontalHeaderItem(0)
        item.setText(self._translate("Dialog", "样品名称"))
        item = self.n_table.horizontalHeaderItem(1)
        item.setText(self._translate("Dialog", "N的个数"))
        item = self.n_table.horizontalHeaderItem(2)
        item.setText(self._translate("Dialog", "Coverage"))
        self.n_table.setRowHeight(0, 100)
        self.n_table.horizontalHeader().setMinimumHeight(60)

    def slot_btn_start(self):
        """
        画图
        :return:
        """
        try:
            for i, path in enumerate(self.path_list):
                path = path.replace('primertrimmed.rg.sorted.bam', 'depth.tsv')
                df = pd.read_table(path, header=None)
                x_axis = df[1].values.tolist()
                y_axis = df[2].values.tolist()
                posi = len(self.path_list) * 100 + 10 + i + 1
                # print(posi, '+++++++++++')
                ax = self.fig.add_subplot(posi)
                ax.cla()
                ax.plot(x_axis, y_axis)
                title = path.split('/')[-1].split('.')[0]
                ax.set_title(title, rotation='horizontal', x=-0.1, y=0.4)
            self.canvas.draw()
        except Exception as e:
            print(e)

    def add_table(self):
        """
        表格添加数据
        :return:
        """
        N_list = self.get_N(self.path_list)
        self.n_table.setRowCount(len(N_list))
        for row, n_data in enumerate(N_list):
            for col, n_ in enumerate(n_data):
                table_item = QtWidgets.QTableWidgetItem()
                self.n_table.setItem(row, col, table_item)
                table_item = self.n_table.item(row, col)
                table_item.setText(self._translate("Dialog", n_))
                table_item.setTextAlignment(Qt.AlignHCenter)
                table_item.setFont(self.font)

    def get_N(self, path_list):
        """
        根据所选文件，获取对应consensus.fasta文件中的N的数量
        :param path_list:
        :return:
        """
        # ['D:/智源代码/高通量测序/1597819658/4.mapping/NB21.primertrimmed.rg.sorted.bam']
        # for path in path_list:
        fasta_path = [*map(lambda x: x.replace('primertrimmed.rg.sorted.bam', 'consensus.fasta'), path_list)]
        N_list = []
        for path in fasta_path:
            if not os.path.exists(path):
                raise FileNotFoundError(f'“{path}”不存在！')
            with open(path, 'r') as f:
                file_con = f.read()
                f.seek(0)
                first_line = f.readline()
                # 读取第一行之后read()就不再包含第一行内容
                file_con = file_con.replace(first_line, '')
                # print(file_con)
                sample_ = path.split('/')[-1].split('.')[0]
                n_count = file_con.count('N')
                n_precent = "%.1f%%" % (100 - (int(n_count) / 29903) * 100)
                N_list.append([sample_, str(n_count), n_precent])
        # print(N_list)
        return N_list


# if __name__ == '__main__':
#     n_list = []
#     app = QApplication(sys.argv)
#     w = QDialog()
#     w_ui = QtDraw()
#     w_ui.init_ui(w)
#     w.exec_()
#     sys.exit(app.exec_())

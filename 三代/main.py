# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 15:28
# @Author  : Lvp
# @File    : main.py
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from mainwindow import Ui_MainWindow
import os
import sqlite3


class MainWindow(QtWidgets.QMainWindow):
    """对QMainWindow类重写，实现一些功能"""

    flag = ''

    conn = sqlite3.connect(f'{os.getcwd()}/sequence.db', check_same_thread=False)
    cursor = conn.cursor()

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现mainwindow窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        content = '是否要退出程序？'
        s_sql = """select taskStatus from task"""
        result = self.cursor.execute(s_sql)
        data = result.fetchall()
        result = ''.join([*map(lambda x: ''.join(x[0]), data)])
        if '开始运行' in result:
            content = '有任务正在运行，退出后当前命令将继续\n在后台运行，是否要退出程序？'
        reply = QtWidgets.QMessageBox.question(self,
                                               '退出程序',
                                               content,
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主窗口
    main = MainWindow()
    main_ui = Ui_MainWindow()
    main_ui.setupUi(main)
    # 显示
    main.show()
    # QMessageBox.warning()
    sys.exit(app.exec_())

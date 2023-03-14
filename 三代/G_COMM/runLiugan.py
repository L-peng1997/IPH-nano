# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 16:23
# @Author  : Lvp
# @File    : runLiugan.py
"""
2021-03-25 16:37:10
流感病毒序列拼接
2021-04-01 09:58:56
temp.fa,temp2.fa,temp2.blastn等文件没有指定结果文件夹路径
所有命令文件仍需检查！！！
"""
import subprocess
import os
import time
import shutil
import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from G_COMM.runXinguan import logger
from configparser import ConfigParser


exepath = os.getcwd().replace('\\', '/')
config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')


class RunLiugan(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        # 窗口传递的参数
        # parmas = [task_type, task_name, self.sample_list, self.barcode_list, file_path]
        logger.info(f'程序运行参数为：{data}')
        self.task_name = data['task_name']

        # 起始路径
        self.ori_path = data['ori_path']
        # 结果路径
        self.result_path = data['result_path']
        # 列表文件
        self.sample_file = data['sample_file']

        # 程序状态
        self.status = '正在运行'

        # 程序运行结果
        self.result = ''
        # 任务类别
        self.task_type = data['task_type']

        # 数据库连接
        self.conn = sqlite3.connect(f'{exepath}/sequence.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_path(self):
        """
        获取当前运行环境的环境变量
        :return:
        """
        path_com = subprocess.Popen('env', stdout=subprocess.PIPE, universal_newlines=True, encoding='utf-8',
                                    shell=True)
        result = path_com.stdout.read()
        logger.info(f'当前环境变量为{result}')

    def liugan(self):
        """
        2023-03-14 23:42:10 流感调整
        """
        try:
            file_comm = f'python {exepath}/G_CONFIG/Flu_Virus/Flu_assemble.py -rawdata  {self.ori_path} -samplelist  {self.sample_file} -result  {self.result_path}'
            logger.info(f'命令如下：{file_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            thi_res = subprocess.run(file_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if thi_res.returncode == 0:
                logger.info('执行成功')
                logger.info(thi_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'执行出错：{thi_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = '执行失败！'
            # self.result = self.status + '：' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            quit()

    def insert_db(self):
        # 运行前将任务参数存储到数据库中
        try:
            db_data = (self.task_name, self.task_type, self.status)
            print(db_data)
            i_sql = """insert into task(taskNm, taskType, taskStatus) values (?,?,?)"""
            self.cursor.execute(i_sql, db_data)
            self.conn.commit()
        except Exception as e:
            self.status = '执行数据入库失败！！！'
            self.result = self.status + '： ' + str(e)
            self.exitSignal.emit(self.result)
            logger.error(f'任务 {self.task_name} {self.status}：{e}')
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            quit()

    def finish(self):
        """
        程序运行结束，关闭数据库连接
        :return:
        """
        self.cursor.close()
        self.conn.close()

    def run(self):
        """
        运行程序
        :return:
        """
        # self.get_path()
        self.insert_db()
        self.liugan()
        # self.status = '已完成' if flag == 0 else f'运行结束，但{"，".join(empty_bar)} 文件夹为空！'
        self.status = '已完成'
        self.exitSignal.emit(self.status)
        # # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()


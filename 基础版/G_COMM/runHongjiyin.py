# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 11:54
# @Author  : Lvp
# @File    : runHongjiyin.py
"""
2021-03-29 11:54:24
宏基因组-序列拼接
宏基因组-查找参考序列
"""
import subprocess
import os
import time
import sqlite3
import shutil
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from G_COMM.runXinguan import logger
from configparser import ConfigParser


exepath = os.getcwd().replace('\\', '/')
config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')


class RunHongjiyin(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        # 窗口传递的参数
        logger.info(f'程序运行参数为：{data}')

        # 任务类别
        self.task_type = data['task_type']

        # 任务名称（结果文件名称/样品名称）
        self.task_name = data['task_name']

        # 序列文件名称
        self.xvlie_path = data['xvlie_path']

        # 数量/测序深度
        self.count = data['count']

        # 起始文件所在文件夹名称
        self.path = data['fastq_file']

        # 获取结果文件存放路径以及数据库路径
        try:
            self.work_file = data['work_file']
            self.work_file = self.work_file + '/' + self.task_name
            if not os.path.exists(self.work_file):
                os.mkdir(self.work_file)
            else:
                shutil.rmtree(self.work_file)
                os.mkdir(self.work_file)
            self.db_path = config.get('Metagenome', 'db_path')
        except Exception as e:
            logger.error(f'读取配置文件失败，{str(e)}')

        # 程序状态
        self.status = '正在运行'

        # 程序运行结果
        self.result = ''

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

    def do_find(self):
        """
        执行python文件中的命令
        :param sample: 样品名称
        :return:
        """
        try:
            sec_comm = f'python {exepath}/G_CONFIG/Metagenome/find_ref_seqs.py -q {self.path} -o {self.work_file} -db {self.db_path} -num {self.count}'
            logger.info(f'命令如下：{sec_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            sec_res = subprocess.run(sec_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if sec_res.returncode == 0:
                logger.info('执行成功')
                logger.info(sec_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'执行出错：{sec_res.stdout}')
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

    def thi_comm(self):
        """
        执行python文件中的命令
        :param sample: 样品名称
        :return:
        """
        try:
            thi_comm = f'python {exepath}/G_CONFIG/Metagenome/ont_meta_assenble.py {self.task_name} {self.path} {self.xvlie_path} {self.work_file} {self.count} '
            logger.info(f'命令如下：{thi_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            thi_res = subprocess.run(thi_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
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
        flag = 0
        if os.path.isfile(self.path):
            if self.task_type == '宏基因组-序列拼接':
                self.thi_comm()
            else:
                self.do_find()
        else:
            flag = 1
        self.status = '已完成' if flag == 0 else f'执行失败，{self.path}错误'
        self.exitSignal.emit(self.status)
        # # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()

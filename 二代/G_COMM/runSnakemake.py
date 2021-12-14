# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 16:55
# @Author  : Lvp
# @File    : runSnakemake.py
"""
诺如病毒
"""
import subprocess
import os
import time
import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from G_COMM.runXinguan import logger
from configparser import ConfigParser

exepath = os.getcwd().replace('\\', '/')

config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')


class RunSnakemake(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data, file_name):
        super().__init__()
        # 窗口传递的参数
        # parmas = [task_type, task_name, self.sample_list, self.barcode_list, file_path]
        logger.info(f'程序运行参数为：{data}')
        self.task_name = data['task_name']
        # 起始文件所在路径
        self.path = data['file_path']
        # self.path = self.work_file
        self.sample_list = data['sample_list']
        self.barcode_list = data['barcode_list']
        self.work_file = data['work_file']
        # if not os.path.exists(self.work_file):
        #     os.mkdir(self.work_file)
        self.count = data['count'] if 'count' in data else 0

        # 程序状态
        self.status = '正在运行'

        # 程序运行结果
        self.result = ''
        # 任务类别
        self.task_type = data['task_type']

        # 数据库连接
        self.conn = sqlite3.connect(f'{exepath}/sequence.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

        # 获取流程文件名称
        try:
            # self.file_name = config.get('Norovirus', 'file_name')
            self.file_name = file_name
        except Exception as e:
            logger.error(f'读取配置文件失败，{str(e)}')

    def get_path(self):
        """
        获取当前运行环境的环境变量
        :return:
        """
        path_com = subprocess.Popen('env', stdout=subprocess.PIPE, universal_newlines=True, encoding='utf-8',
                                    shell=True)
        result = path_com.stdout.read()
        logger.info(f'当前环境变量为{result}')

    def copy_file(self):
        cp_comm = f'cp {exepath}/G_CONFIG/{self.file_name} {self.path}'
        logger.info(f'复制文件的命令如下：{cp_comm}')
        try:
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行 cp命令'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            cp_res = subprocess.run(cp_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    universal_newlines=True, shell=True)
            if cp_res.returncode == 0:
                logger.info('复制文件 执行成功')
                logger.info(cp_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'复制文件 执行出错：{cp_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = '复制文件 执行失败！'
            self.result = self.status + '：' + str(e.stderr)
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            quit()

    def unlock(self):
        """
        解锁文件
        :return:
        """
        unlock_comm = f'snakemake -s {self.path}/{self.file_name} --config path={self.path} --unlock --cores 1'
        logger.info(f'命令如下：{unlock_comm}')
        try:
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行 unlock'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            unlock_res = subprocess.run(unlock_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        universal_newlines=True, shell=True)
            if unlock_res.returncode == 0:
                logger.info('unlock  执行成功')
                logger.info(unlock_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'unlock  执行出错：{unlock_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'unlock 执行失败！'
            # self.result = self.status + '：' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            quit()

    def nuoru_comm(self):
        """
        执行诺如病毒命令
        :param path: 目标文件路径
        :return:
        """
        nuoru_comm = f'snakemake -s {self.path}/{self.file_name} --config path={self.path} count={self.count}  -j 4 -F'
        logger.info(f'命令如下：{nuoru_comm}')
        try:
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)
            # time.sleep(10)

            nuoru_res = subprocess.run(nuoru_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       universal_newlines=True, shell=True)
            if nuoru_res.returncode == 0:
                logger.info('执行成功')
                logger.info(nuoru_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'执行出错：{nuoru_res.stdout}')
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
        self.copy_file()
        # self.unlock()
        self.nuoru_comm()
        self.status = '已完成'
        self.exitSignal.emit(self.status)
        # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()

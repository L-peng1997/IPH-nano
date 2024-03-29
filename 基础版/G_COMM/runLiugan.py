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
import sys
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
        # 起始文件所在路径
        # self.ori_name = config.get('Flu_Virus', 'ori_name')
        self.path = data['fastq_file']
        # 样品名称
        self.sample_name = data['task_name']

        # self.sample_list = data['sample_list']
        # self.barcode_list = data['barcode_list']

        # 获取结果文件存放路径以及数据库路径
        try:
            self.work_file = data['work_file']
            self.work_file = self.work_file + '/' + self.task_name
            print(self.work_file)
            if not os.path.exists(self.work_file):
                os.mkdir(self.work_file)
            else:
                shutil.rmtree(self.work_file)
                os.mkdir(self.work_file)
            self.db_path = config.get('Flu_Virus', 'db_path')
        except Exception as e:
            logger.error(f'读取配置文件失败，{str(e)}')

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

    def merge_file(self, sample, barcode):
        """
        合并barcode文件夹下的所有文件
        :param sample: 样品名称
        :param barcode: barcode文件夹
        :return:
        """
        if not os.path.exists(self.work_file + "/" + self.fastq_name):
            os.mkdir(self.work_file + "/" + self.fastq_name)
        try:
            cat_comm = f'cat {self.path}/{barcode}/*.fastq > {self.work_file + "/" + self.fastq_name}/{sample}.fastq'
            logger.info(f'合并文件的命令如下：{cat_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=?  and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在合并文件'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)
            # time.sleep(10)

            cat_res = subprocess.run(cat_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if cat_res.returncode == 0:
                logger.info('合并文件 执行成功')
                logger.info(cat_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'合并文件 执行出错：{cat_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = '合并文件 执行失败！'
            self.result = self.status + '：' + str(e.stderr)
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=?  and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            sys.exit()

    def secnod_comm(self):
        """
        执行python文件中的命令
        :param sample: 样品名称
        :return:
        """
        try:
            # sec_comm = f'python {exepath}/G_CONFIG/Flu_Virus/ont_flu_8segments_assemble.py -d {self.work_file + "/" + self.fastq_name} -o {self.work_file} -db {self.db_path} -s {sample}'
            sec_comm = f'python {exepath}/G_CONFIG/Flu_Virus/ont_flu_8segments_assemble.py -d {self.path} -o {self.work_file} -db {self.db_path} -s {self.sample_name}'
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
            sys.exit()

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
            sys.exit()

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
        if os.path.exists(self.path):
            self.secnod_comm()
        else:
            flag = 1
        # self.status = '已完成' if flag == 0 else f'运行结束，但{"，".join(empty_bar)} 文件夹为空！'
        self.status = '已完成' if flag == 0 else f'运行结束，但{self.path} 文件不存在！'
        self.exitSignal.emit(self.status)
        # # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()


# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 18:22
# @Author  : Lvp
# @File    : runDatacontrol.py
"""
二代测序-数据质控
"""
import os
import sqlite3
import subprocess
from configparser import ConfigParser
from datetime import datetime
import pandas as pd
from PyQt5.QtCore import QObject, pyqtSignal
from G_COMM.runXinguan import logger
import shutil

# 获取执行路径，方便后续读取配置文件
exepath = os.getcwd().replace('\\', '/')

config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')


class RunDataControl(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        # 窗口传递的参数
        # {'task_type': 'Dialog', 'task_name': '111', 'xvlie_path': '222',
        # 'sample_list': '', 'barcode_list': '', 'work_file': '111', 'platform': 'illumina',
        # 'cexv_type': 'single', 'trim_front1': '12', 'trim_tail1': '24',
        # 'trim_front2': '', 'trim_tail2': ''}
        logger.info(f'程序运行参数为：{data}')
        self.task_name = data['task_name']
        # 起始文件所在路径
        self.start_file = data['work_file']
        # 样品列表文件
        self.sample_list = data['sample_list']
        # 测序平台
        self.platform = data['platform']
        # 测序类型
        self.cexv_type = data['cexv_type']
        # 序列修剪1
        self.trim_front1 = data['trim_front1']
        self.trim_tail1 = data['trim_tail1']
        # 序列修剪2
        self.trim_front2 = data['trim_front2']
        self.trim_tail2 = data['trim_tail2']

        try:
            # 第一步结果文件夹名称:0.rawdata
            self.fir_file = config.get('Quality_Control', 'fir_file')
            if not os.path.exists(f'{self.start_file}/{self.fir_file}'):
                os.mkdir(f'{self.start_file}/{self.fir_file}')
            # 第二步结果文件夹名称:1.cutadapt
            self.sec_file = config.get('Quality_Control', 'sec_file')
            if not os.path.exists(f'{self.start_file}/{self.sec_file}'):
                os.mkdir(f'{self.start_file}/{self.sec_file}')
            # 在第二部结果文件下创建report文件夹
            if not os.path.exists(f'{self.start_file}/{self.sec_file}/report'):
                os.mkdir(f'{self.start_file}/{self.sec_file}/report')
            # 起始文件夹指定文件后缀
            file_exten = config.get('Quality_Control', 'rawdata')
            self.file_exten_list = file_exten.split(',')
            # qc后缀
            qc_exten = config.get('Quality_Control', 'qc')
            self.qc_exten_list = qc_exten.split(',')

            self.adapter_sequence = config.get('Quality_Control', 'adapter_sequence')
            self.adapter_sequence_r2 = config.get('Quality_Control', 'adapter_sequence_r2')
        except Exception as e:
            logger.error(f'获取配置文件失败：{e}')

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

    def judge_format(self):
        """
        根据配置文件中的rawdata后缀来判断起始文件夹是否可用
        若可用则将符合要求的文件复制到新建文件夹0.rawdata下
        否则报错
        :return:
        """
        request_data = []
        if os.path.exists(self.start_file):
            file_list = os.listdir(self.start_file)
            for file in file_list:
                if file.endswith(self.file_exten_list[0]) or file.endswith(self.file_exten_list[1]):
                    request_data.append(file)

            if not os.path.exists(f'{self.start_file}/{self.fir_file}'):
                os.mkdir(f'{self.start_file}/{self.fir_file}')
            if len(request_data) >= 1:
                for r_file in request_data:
                    shutil.copy(f'{self.start_file}/{r_file}', f'{self.start_file}/{self.fir_file}')
        else:
            self.result = '起始文件夹格式存在错误，请核对文件类型及名称'
            self.status = '执行失败！'
            self.exitSignal.emit(self.result)
            logger.error(f'任务 {self.task_name} {self.status}：{self.result}')
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            quit()

    def run_comm(self, sample_name):
        """
        运行python命令
        :return:
        """
        if self.cexv_type == 'single':
            run_comm = f'fastp -i {self.start_file}/{self.fir_file}/{sample_name}{self.file_exten_list[0]} -f {self.trim_front1} -t {self.trim_tail1} ' \
                f'-o {self.start_file}/{self.sec_file}/{sample_name}{self.qc_exten_list[0]} -h {self.start_file}/{self.sec_file}/report/{sample_name}.html -j {self.start_file}/{self.sec_file}/report/{sample_name}.json'
        elif self.cexv_type == 'double':
            run_comm = f'fastp -i {self.start_file}/{self.fir_file}/{sample_name}{self.file_exten_list[0]} -I {self.start_file}/{self.fir_file}/{sample_name}{self.file_exten_list[1]} -o {self.start_file}/{self.sec_file}/{sample_name}{self.qc_exten_list[0]} -O {self.start_file}/{self.sec_file}/{sample_name}{self.qc_exten_list[1]} -f {self.trim_front1} -F {self.trim_front2} ' \
                f'-t {self.trim_tail1} -T {self.trim_tail2} -h {self.start_file}/{self.sec_file}/report/{sample_name}.html -j {self.start_file}/{self.sec_file}/report/{sample_name}.json'

        if self.platform == 'huada':
            run_comm += f'--adapter_sequence {self.adapter_sequence} --adapter_sequence_r2 {self.adapter_sequence_r2}'

        try:
            # sec_comm = f'python {exepath}/G_CONFIG/Metagenome/find_ref_seqs.py -q {self.path} -o {self.work_file}/{self.task_name}.fa -db {self.db_path} -num {self.count}'
            logger.info(f'命令如下：{run_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            comm_res = subprocess.run(run_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if comm_res.returncode == 0:
                logger.info('执行成功')
                logger.info(comm_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'执行出错：{comm_res.stdout}')
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
        self.judge_format()
        self.insert_db()
        for sample_name in self.sample_list:
            self.run_comm(sample_name)
        self.status = '已完成'
        self.exitSignal.emit(self.status)
        # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()

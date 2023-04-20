# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 16:55
# @Author  : Lvp
# @File    : RunWeizhi.py
"""
未知病毒
2021-03-26 11:46:21
修改程序同新冠测序一致，但由于运行一次占内存较大，故不使用多任务同时运行
"""
import subprocess
import os
import sys
import time
import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from G_COMM.runXinguan import logger
from configparser import ConfigParser
from webShow import WebShow

exepath = os.getcwd().replace('\\', '/')

config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')


class RunWeizhi(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        # 窗口传递的参数
        # parmas = [task_type, task_name, self.sample_list, self.barcode_list, file_path]
        logger.info(f'程序运行参数为：{data}')
        self.task_name = data['task_name']
        # 起始文件所在路径
        self.fir_name = config.get('Unknown_Path', 'fir_name')
        # barcode文件父级路径
        self.path = data['file_path'] + '/' + self.fir_name

        self.sample_list = data['sample_list']
        self.barcode_list = data['barcode_list']

        # 程序状态
        self.status = '正在运行...'

        # 程序运行结果
        self.result = ''
        # 任务类别
        self.task_type = data['task_type']

        # 数据库连接
        self.conn = sqlite3.connect(f'{exepath}/sequence.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

        # 获取结果文件存放路径以及数据库路径
        try:
            self.work_file = config.get('Unknown_Path', 'work_file')
            self.work_file = self.work_file + '/' + self.task_name if self.work_file else self.path
            self.db_path = config.get('Unknown_Path', 'db_path')
            # 将结果文件夹存放在任务名称文件夹下
            self.sec_name = config.get('Unknown_Path', 'sec_name')
            self.thi_name = config.get('Unknown_Path', 'thi_name')
            self.for_name = config.get('Unknown_Path', 'for_name')
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

    def merge_file(self, sample, barcode):
        """
        合并barcode文件夹下的所有文件
        :param sample: 样品名称
        :param barcode: barcode文件夹
        :return:
        """
        try:

            cat_comm = f'cat {self.path}/{barcode}/*.fastq > {self.work_file + "/" + self.sec_name}/{sample}.fastq'
            logger.info(f'合并文件的命令如下：{cat_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行 cat命令'
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
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            sys.exit()

    def secnod_comm(self, sample):
        """
        执行centrifuge命令
        :return:
        """
        try:
            # sec_comm = f'centrifuge -p 8 -x /public/hpvc -U {self.work_file + "/" + self.sec_name}/{barcode}.fastq -S {self.work_file + "/" + self.thi_name}/{barcode}.tsv --report-file {self.work_file + "/" + self.thi_name}/{barcode}_report.tsv'
            sec_comm = f'kraken2 --db {self.db_path} --classified-out {self.work_file + "/" + self.thi_name}/{sample}.classified --threads 20 --report {self.work_file + "/" + self.for_name}/{sample}.report --output {self.work_file + "/" + self.for_name}/{sample}.kraken {self.work_file + "/" + self.sec_name}/{sample}.fastq'
            logger.info(f'命令如下：{sec_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行 kraken2'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            sec_res = subprocess.run(sec_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if sec_res.returncode == 0:
                logger.info('centrifuge  执行成功')
                logger.info(sec_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'centrifuge  执行出错：{sec_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'centrifuge 执行失败！'
            # self.result = self.status + '：' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            sys.exit()

    def thi_comm(self, barcode):
        """
        执行centrifuge-kreport命令
        :return:
        """
        try:
            thi_comm = f'centrifuge-kreport -x /public/hpvc {self.work_file + "/" + self.thi_name}/{barcode}_report.tsv > {self.work_file + "/" + self.for_name}/{barcode}_kraken.tsv'
            logger.info(f'命令如下：{thi_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行 centrifuge-kreport'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            thi_res = subprocess.run(thi_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if thi_res.returncode == 0:
                logger.info('centrifuge-kreport 执行成功')
                logger.info(thi_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'centrifuge-kreport 执行出错：{thi_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'centrifuge-kreport 执行失败！'
            # self.result = self.status + '：' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            sys.exit()

    def run_R(self):
        try:
            for_comm = f'Rscript {exepath}/G_CONFIG/runapp.R > {exepath}/G_CONFIG/R.log 2>&1 &'
            logger.info(f'命令如下：{for_comm}')

            for_res = subprocess.run(for_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if for_res.returncode == 0:
                logger.info('Rscript 执行成功')
                logger.info(for_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'Rscript 执行出错：{for_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'Rscript 执行失败！'
            self.result = self.status + '：' + str(e.stderr)
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
        # 根据任务名称创建结果文件夹，防止后续创建文件夹时路径不存在
        if not os.path.exists(self.work_file):
            os.mkdir(self.work_file)
        # 创建每一步命令的结果文件夹，此时的文件名称为：任务名 + 步骤名，
        # 例如：self.task_name + '/' + self.sec_name
        if not os.path.exists(self.work_file + '/' + self.sec_name):
            os.mkdir(self.work_file + '/' + self.sec_name)
        if not os.path.exists(self.work_file + '/' + self.thi_name):
            os.mkdir(self.work_file + '/' + self.thi_name)
        if not os.path.exists(self.work_file + '/' + self.for_name):
            os.mkdir(self.work_file + '/' + self.for_name)
        # self.get_path()
        self.insert_db()
        # barcode_list = os.listdir(self.path)
        # print(barcode_list)
        flag = 0
        empty_bar = []
        for sample, bar in zip(self.sample_list, self.barcode_list):
            if os.path.exists(f'{self.path}/{bar}') and not len(os.listdir(f'{self.path}/{bar}')) == 0:
                self.merge_file(sample, bar)
                self.secnod_comm(sample)
            else:
                flag = 1
                empty_bar.append(bar)
                logger.info(f'{self.path}/{bar} 文件夹为空！')
        self.run_R()
        self.status = '已完成' if flag == 0 else f'运行结束，但{"，".join(empty_bar)} 文件夹为空！'
        self.exitSignal.emit(self.status)
        # # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()
        try:
            a = WebShow()
            a.open_weizhi()
        except Exception as e:
            print('网页打开错误', e)
            logger.error(f'网页打开错误：{e}')

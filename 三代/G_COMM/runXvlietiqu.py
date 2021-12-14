# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 15:08
# @Author  : Lvp
# @File    : runXvlietiqu.py
"""
Nanopore未知病原-序列提取
"""
import subprocess
import os
import time
import sqlite3
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from G_COMM.runXinguan import logger
from configparser import ConfigParser
import pandas as pd

exepath = os.getcwd().replace('\\', '/')

config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')


class RunPython(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        # 窗口传递的参数
        # parmas = [task_type, task_name, self.sample_list, self.barcode_list, file_path]
        logger.info(f'程序运行参数为：{data}')
        self.task_name = data['task_name']
        # 起始文件所在路径
        self.fastq_file = data['fastq_file']

        self.tsv_file = data['tsv_file']
        self.txid = data['txid']
        self.result_file = data['work_file']
        if not os.path.exists(self.result_file):
            os.mkdir(self.result_file)
        self.task_name = data['task_name']

        # 程序状态
        self.status = '正在运行'

        # 程序运行结果
        self.result = ''
        # 任务类别
        self.task_type = data['task_type']

        # 数据库连接
        self.conn = sqlite3.connect(f'{exepath}/sequence.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

        # 读取txid
        self.table1 = ''

    def get_path(self):
        """
        获取当前运行环境的环境变量
        :return:
        """
        path_com = subprocess.Popen('env', stdout=subprocess.PIPE, universal_newlines=True, encoding='utf-8',
                                    shell=True)
        result = path_com.stdout.read()
        logger.info(f'当前环境变量为{result}')

    def run_taxonkit(self):
        try:
            taxonkit_comm = f"taxonkit list --ids {self.txid} > list"
            logger.info(f'taxonkit 的命令如下：{taxonkit_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行 taxonkit命令'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            cat_res = subprocess.run(taxonkit_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if cat_res.returncode == 0:
                logger.info('taxonkit 执行成功')
                self.table1 = pd.read_csv("./list", names=["id"])
            else:
                self.status = '执行失败！'
                logger.error(f'taxonkit 执行出错：{cat_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'taxonkit 执行失败！'
            self.result = self.status + '：' + str(e.stderr)
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            quit()

    def merage_file(self):
        table2 = pd.read_csv(self.tsv_file, names=["comfirm", "readsid", "id", "length", "detail"], sep="\t")
        logger.info(f'{self.tsv_file}的内容为：{table2}')
        table3 = pd.merge(table2, self.table1, on="id", how="inner")
        logger.info(f'合并后的内容为：{table3}')
        logger.info(f"{self.result_file}/temp_seqlist.txt")
        with open(f"{self.result_file}/temp_seqlist.txt", "a") as ww:
            for name in table3["readsid"]:
                ww.write(name + "\n")

    def run_seqkit(self):
        """
        执行序列提取文件
        :param:
        :return:
        """
        try:
            seqkit_comm = f"seqkit grep -f {self.result_file}/temp_seqlist.txt {self.fastq_file}>{self.result_file}/{self.task_name}.fastq"
            seqkit_comm1 = f"seqkit fq2fa {self.result_file}/{self.task_name}.fastq -o {self.result_file}/{self.task_name}.fa"
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行 seqkit'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)
            # time.sleep(10)

            seqkit_res = subprocess.run(seqkit_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            seqkit_res1 = subprocess.run(seqkit_comm1, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if seqkit_res.returncode == 0 and seqkit_res1.returncode == 0:
                logger.info('seqkit 执行成功')
                logger.info(seqkit_res.stdout)
                logger.info(seqkit_res1.stdout)
                os.remove(f"{self.result_file}/temp_seqlist.txt")
            else:
                self.status = '执行失败！'
                logger.error(f'seqkit 执行出错：{seqkit_res.stdout}')
                logger.error(f'seqkit 执行出错：{seqkit_res1.stdout}')
        except Exception as e:
            self.status = 'seqkit 执行失败！'
            # self.result = self.status + '：' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e}')
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
        if self.txid.isdigit():
            self.run_taxonkit()
        else:
            self.table1 = pd.read_csv(self.txid, names=["id"])
        logger.info(self.table1)
        self.merage_file()
        self.run_seqkit()
        self.status = '已完成'
        self.exitSignal.emit(self.status)
        # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()

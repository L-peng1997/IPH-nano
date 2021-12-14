# -*- coding:utf-8 -*-
# @Time: 2021/6/29 12:14
# @Author: Lvp
"""
二代测序-序列拼接(基于参考序列)
"""
import os
import sqlite3
import subprocess
from configparser import ConfigParser
from datetime import datetime
from PyQt5.QtCore import QObject, pyqtSignal
from G_COMM.runXinguan import logger
import shutil

# 获取执行路径，方便后续读取配置文件
exepath = os.getcwd().replace('\\', '/')

config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')


class RunErdaixlpj(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        # 窗口传递的参数
        # {'task_type': '二代测序-序列拼接(基于参考序列)', 'task_name': '222',
        # 'sample_list': ['111'], 'barcode_list': '', 'work_file': '222',
        # 'cexv_type': 'single', 'xvlie_file': 'D:/工程文档/疾病预防控制中心/广东省疾控公共卫生研究院/高通量测序分析平台/21需求管理(RD&REQM)/代码文件/test.txt', '
        # snp': '0.1', 'threads': '10', 'depth': '10', 'quality': '20'}
        logger.info(f'程序运行参数为：{data}')
        self.task_name = data['task_name']
        # 起始文件所在路径
        self.start_file = data['work_file']
        # 参考序列文件路径
        self.xvlie_file = data['xvlie_file']
        # 样品列表文件
        self.sample_list = data['sample_list']
        # 测序类型
        self.cexv_type = data['cexv_type']
        # SNP阈值
        self.snp = data['snp']
        # 线程数
        self.threads = data['threads']
        # 测序深度阈值
        self.depth = data['depth']
        # 测序质量阈值
        self.quality = data['quality']

        try:
            # 第二步结果文件夹名称:1.cutadapt
            self.sec_file = config.get('Quality_Control', 'sec_file')
            # 第三步结果文件夹名称:2.mapping
            self.thi_file = config.get('Quality_Control', 'thi_file')
            if not os.path.exists(f'{self.start_file}/{self.thi_file}'):
                os.mkdir(f'{self.start_file}/{self.thi_file}')
            # qc后缀
            qc_exten = config.get('Quality_Control', 'qc')
            self.qc_exten_list = qc_exten.split(',')
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

    def judge_format(self):
        """
        判断该路径下是否含有1.cutadapt文件夹，其中的文件应以samplename.fp_1.fq.gz方式命名
        :return:
        """
        request_data = []
        if os.path.exists(f'{self.start_file}/{self.sec_file}'):
            file_list = os.listdir(f'{self.start_file}/{self.sec_file}')
            for file in file_list:
                if file.endswith(self.qc_exten_list[0]) or file.endswith(self.qc_exten_list[1]):
                    request_data.append(file)

        if len(request_data) == 0:
            self.result = f'请确定{self.start_file}路径下是否含有1.cutadapt文件夹，其中的文件应以samplename.fp_1.fq.gz方式命名'
            self.status = '起始文件判断失败!'
            self.exitSignal.emit(self.result)
            logger.error(f'任务 {self.task_name} {self.status}：{self.result}')
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            quit()

    def get_path(self):
        """
        获取当前运行环境的环境变量
        :return:
        """
        path_com = subprocess.Popen('env', stdout=subprocess.PIPE, universal_newlines=True, encoding='utf-8',
                                    shell=True)
        result = path_com.stdout.read()
        logger.info(f'当前环境变量为{result}')

    def run_python(self, sample_name):
        """
        执行python文件命令
        :return:
        """
        try:
            # python assemble_seq.py -type {} -ref {} -sample_name {} -threads {} -depth {} -quality {} -snp_cutoff
            sec_comm = f'python {exepath}/G_CONFIG/erdai/assemble_seq.py -type {self.cexv_type} -ref {self.xvlie_file} -sample_name {sample_name} ' \
                f'-threads {self.threads} -depth {self.depth} -quality {self.quality} -snp_cutoff {self.snp} ' \
                f'-sec_file {self.start_file}/{self.sec_file} -thi_file {self.start_file}/{self.thi_file}'
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
            self.run_python(sample_name)
            # print(sample_name)
        self.status = '已完成'
        self.exitSignal.emit(self.status)
        # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()











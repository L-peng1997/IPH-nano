# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 15:59
# @Author  : Lvp
# @File    : runXinguan.py
"""
新冠：序列拼接
"""
import subprocess
import os
import sys
from configparser import ConfigParser
import threading
import time
import re
import shlex
import sqlite3
from loguru import logger
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime

logger.add('./logs/task.log', rotation="500 MB", retention='7 days')

exepath = os.getcwd().replace('\\', '/')
# 默认为当前路径
# base_path = os.getcwd()
config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')

sem = threading.Semaphore(4)  # 限制线程的最大数量为4个


class RunCommand(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data):
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

        # 结果文件所在路径
        try:
            self.work_file = config.get('SARS-COV-2', 'work_file')
            if not os.path.exists(self.work_file):
                os.mkdir(self.work_file)
            self.fir_name = config.get('SARS-COV-2', 'fir_name')
            # 将结果文件夹存放在任务名称文件夹下
            self.sec_name = self.task_name + '/' + config.get('SARS-COV-2', 'sec_name')
            self.thi_name = self.task_name + '/' + config.get('SARS-COV-2', 'thi_name')
            self.for_name = self.task_name + '/' + config.get('SARS-COV-2', 'for_name')
            self.thi_name_re = self.task_name + '/' + config.get('SARS-COV-2', 'thi_name_re')
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
        path_com = subprocess.Popen('env', stdout=subprocess.PIPE, universal_newlines=True, encoding='utf-8', shell=True)
        result = path_com.stdout.read()
        logger.info(f'当前环境变量为{result}')

    def first_comm(self, path):
        """
        执行第一条命令:guppy_basecaller
        :param path: fast5目录的路径，如：./fast5/
        :return:
        """
        # global fir_res
        try:
            fir_comm = f'guppy_basecaller -c dna_r9.4.1_450bps_hac.cfg -i {path} -s {self.work_file + "/" + self.sec_name} -x auto -r'
            logger.info(f'命令如下：{fir_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行 guppy_basecaller'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            fir_res = subprocess.run(fir_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if fir_res.returncode == 0:
                logger.info('guppy_basecaller执行成功')
                logger.info(fir_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'guppy_basecaller执行出错：{fir_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'guppy_basecaller执行失败！'
            # self.result = self.status + '：' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            sys.exit()

    def second_comm(self, file):
        """
        执行第二条命令
        :return:
        """
        # 判断第四步命令结果文件夹是否存在，如不存在则创建
        if not os.path.exists(self.work_file + '/' + self.for_name):
            os.mkdir(self.work_file + '/' + self.for_name)
        try:
            sec_comm = f'guppy_barcoder --require_barcodes_both_ends -i {file} -s {self.work_file + "/" + self.thi_name} --arrangements_files "barcode_arrs_nb12.cfg barcode_arrs_nb24.cfg"'
            logger.info(f'命令如下：{sec_comm}')
            # 将当前任务状态更新到数据库中，以便页面展示
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            self.status = '正在运行 guppy_barcoder'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            sec_res = subprocess.run(sec_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if sec_res.returncode == 0:
                logger.info('guppy_barcoder执行成功')
                logger.info(sec_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'guppy_barcoder执行出错：{sec_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'guppy_barcoder执行失败！'
            # self.result = self.status + '：' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            sys.exit()

    def third_comm(self, conn, cursor, thi_path, sample, bar):
        """
        执行第三条命令
        :param thi_path: 结果文件夹路径
        :param sample: 样品名称
        :param bar: 标签名称
        :return:
        """
        num = re.findall(r'\d+', bar)[0]
        try:
            thi_comm = f'artic guppyplex --skip-quality-check --min-length 400 --max-length 700 --directory {thi_path}/{bar} --output {self.work_file + "/" + self.thi_name_re}/{sample + num}.fastq'
            logger.info(f'命令如下: {thi_comm}')
            # 将当前任务状态更新到数据库中，以便页面展示
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            self.status = '正在运行 artic guppyplex'
            cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            conn.commit()
            self.exitSignal.emit(self.status)
            # time.sleep(5)

            thi_res = subprocess.run(thi_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            if thi_res.returncode == 0:
                logger.info('artic guppyplex执行成功')
                logger.info(thi_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'artic guppyplex执行出错：{thi_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'artic guppyplex执行失败！'
            # self.result = self.status + '： ' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            logger.error(f'任务 {self.task_name, sample, bar} {self.status}：{e.stderr}')
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            conn.commit()
            sys.exit()

    def forth_comm(self, conn, cursor, sample, bar):
        """
        执行第四步命令
        :param sample: 样品名称
        :param bar: 标签名称
        :return:
        """
        num = re.findall(r'\d+', bar)[0]
        try:
            for_comm = f'artic minion --medaka --normalise 200 --threads 10 --scheme-directory {exepath}/artic-ncov2019/primer_schemes --read-file {self.work_file + "/" + self.thi_name_re}/{sample + num}.fastq nCoV-2019/V3 {self.work_file + "/" + self.for_name}/{sample + num}'
            logger.info(f'命令如下：{for_comm}')
            # 将当前任务状态更新到数据库中，以便页面展示
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            self.status = '正在运行 artic minion'
            cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            conn.commit()
            self.exitSignal.emit(self.status)
            # time.sleep(5)

            for_res = subprocess.run(for_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            logger.info(for_res.stdout)
            if for_res.returncode == 0:
                logger.info('artic minion 执行成功')
                logger.info(for_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'artic minion执行出错：{for_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'artic minion 执行失败！'
            # self.result = self.status + '： ' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            logger.error(f'任务 {self.task_name, sample, bar} {self.status}：{e.stderr}')
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            conn.commit()
            sys.exit()

    def get_tsv(self, conn, cursor, sample, bar):
        """
        对结果文件进行分析，以便后续折线图的展示
        :param sample: 样品名称
        :param bar: barcode
        :return:
        """
        num = re.findall(r'\d+', bar)[0]
        try:
            fif_com = f'samtools depth {self.work_file + "/" + self.for_name}/{sample + num}.primertrimmed.rg.sorted.bam>{self.work_file + "/" + self.for_name}/{sample + num}.depth.tsv'
            logger.info(f'命令如下：{fif_com}')
            # 将当前任务状态更新到数据库中，以便页面展示
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            self.status = '正在运行 samtools depth'
            cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            conn.commit()
            self.exitSignal.emit(self.status)
            # 执行命令
            fif_res = subprocess.run(fif_com, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     universal_newlines=True, shell=True)
            logger.info(fif_res.stdout)
            if fif_res.returncode == 0:
                logger.info('samtools 执行成功')
                logger.info(fif_res.stdout)
            else:
                self.status = '执行失败！'
                logger.error(f'samtools 执行出错：{fif_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = 'samtools 执行失败！'
            # self.result = self.status + '： ' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            logger.error(f'任务 {self.task_name, sample, bar} {self.status}：{e.stderr}')
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            conn.commit()
            sys.exit()

    def move_file(self, conn, cursor, sample, bar):
        """
        复制部分结果文件到单独的文件夹
        :param sample: 样品名称
        :param bar: barcode
        :return:
        """
        num = re.findall(r'\d+', bar)[0]
        result_file = config.get('SARS-COV-2', 'result_file').split(',')
        results = [*map(lambda x: sample + num + x, result_file)]
        try:
            # 将当前任务状态更新到数据库中，以便页面展示
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            self.status = '正在运行 复制结果文件'
            cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            conn.commit()
            self.exitSignal.emit(self.status)
            for result in results:
                cp_file = f'cp {self.work_file + "/" + self.for_name}/{result} {self.work_file + "/" + self.for_name}/results'
                logger.info(f'命令如下：{cp_file}')
                # 执行命令
                fif_res = subprocess.run(cp_file, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                         universal_newlines=True, shell=True)
                logger.info(fif_res.stdout)
                if fif_res.returncode == 0:
                    logger.info('复制结果文件 执行成功')
                    logger.info(fif_res.stdout)
                else:
                    self.status = '执行失败！'
                    logger.error(f'复制结果文件 执行出错：{fif_res.stdout}')
        except subprocess.CalledProcessError as e:
            self.status = '复制结果文件 执行失败！'
            # self.result = self.status + '： ' + str(e.stderr)
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            logger.error(f'任务 {self.task_name, sample, bar} {self.status}：{e.stderr}')
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            conn.commit()
            sys.exit()

    def thi_to_fifth(self, thi_path, sample, bar):
        """
        开启多线程运行第三、四、五步命令
        :param thi_path: 第三步命令结果文件夹路径
        :param sample: 样品名称
        :param bar: barcode
        :return:
        """
        conn = sqlite3.connect(f'{exepath}/sequence.db', check_same_thread=False)
        cursor = conn.cursor()
        logger.info(f'当前运行的样品为{sample}，标签为{bar}')

        if len(os.listdir(f'{thi_path}/{bar}')) != 0:

            logger.info('正在运行第三条命令')
            self.third_comm(conn, cursor, thi_path, sample, bar)

            logger.info('正在运行第四条命令')
            self.forth_comm(conn, cursor, sample, bar)

            logger.info('正在运行第五条命令')
            self.get_tsv(conn, cursor, sample, bar)

            logger.info('开始复制结果文件')
            self.move_file(conn, cursor, sample, bar)

            # cursor.close()
            # conn.close()

            sem.release()

    def multi_thread(self, thi_path, list1, list2):
        """
        开启多线程运行第三、四、五步命令
        :param thi_path: 第三步命令结果文件夹路径
        :param list1: 样品名称列表
        :param list2: barcode列表
        :return:
        """
        # 多线程列表，为了方便后边循环join
        threads = []
        if len(list1) >= 4:
            for sample, bar in zip(list1, list2):
                sem.acquire()
                thread1 = threading.Thread(target=self.thi_to_fifth, args=(thi_path, sample, bar), name='xinguan')
                thread1.start()
                threads.append(thread1)
                # print(threading.activeCount())
        else:
            for sample, bar in zip(list1, list2):
                self.thi_to_fifth(thi_path, sample, bar)

        # 循环对线程执行join操作，等待所有线程结束后，在执行主线程的程序
        for t in threads:
            t.join()

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

    def run(self, flag):
        """
        运行程序
        :return:
        """
        # 获取当前运行环境的环境变量
        # self.get_path()
        # 从第一步开始
        # print(datetime.now())
        self.insert_db()
        # 创建命令结果文件存放文件夹
        if not os.path.exists(self.work_file + '/' + self.task_name):
            os.mkdir(self.work_file + '/' + self.task_name)
        # 判断第三、四步命令结果文件夹是否存在，如不存在则创建
        if not os.path.exists(self.work_file + '/' + self.for_name):
            os.mkdir(self.work_file + '/' + self.for_name)
        if not os.path.exists(self.work_file + '/' + self.thi_name_re):
            os.mkdir(self.work_file + '/' + self.thi_name_re)
        if not os.path.exists(self.work_file + "/" + self.for_name + '/results'):
            os.mkdir(self.work_file + "/" + self.for_name + '/results')
        if flag == 1:
            # 向窗口发送运行中...信号，在窗口退出时提醒有任务正在运行
            self.exitSignal.emit(self.status)
            logger.info(f'命令开始执行，路径如下{self.path}')
            logger.info('正在运行第一条命令')
            first_path = self.path + f'/{self.fir_name}/'
            self.first_comm(first_path)
            logger.info('正在运行第二条命令')
            sec_path = self.work_file + f'/{self.sec_name}/'
            self.second_comm(sec_path)
            thi_path = self.work_file + f"/{self.thi_name}"

            self.multi_thread(thi_path, self.sample_list, self.barcode_list)

            self.status = '已完成'
            # 向窗口发送已完成信号，在窗口退出时只提醒是否确认退出
            self.exitSignal.emit(self.status)
            # print('程序结束！！！')
        # 从第三步开始
        elif flag == 3:
            logger.info(f'命令开始执行，路径如下{self.path}')
            self.exitSignal.emit(self.status)
            thi_path = self.path + f"/{config.get('SARS-COV-2', 'thi_name')}"

            self.multi_thread(thi_path, self.sample_list, self.barcode_list)
            self.status = '已完成'
            # 向窗口发送已完成信号，在窗口退出时只提醒是否确认退出
            self.exitSignal.emit(self.status)
            # print('程序结束！！！')
        else:
            logger.error(f'启动错误：flag值为{flag}')
        # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()
        # print(datetime.now())


if __name__ == '__main__':
    task = str(int(time.time()))
    # base_path = os.getcwd()
    task_name = input('任务名称：')
    base_path = input('路径：')
    sample_list = shlex.split(input('样品名称：'))
    barcode_list = shlex.split(input('barcode：'))
    data = {
        'task_name': task_name,
        'file_path': base_path,
        'sample_list': sample_list,
        'barcode_list': barcode_list,
        'task_type': 'Nanopore新冠病毒',
    }
    A = RunCommand(data)
    A.run(3)

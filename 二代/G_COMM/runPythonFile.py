import subprocess
import os
import time
import sqlite3
import shutil
import traceback
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from G_COMM.runXinguan import logger
from configparser import ConfigParser


exepath = os.getcwd().replace('\\', '/')
config = ConfigParser()
config.read(f'{exepath}/G_CONFIG/config.ini', encoding='utf-8')


class RunPythonFile(QObject):
    # 向窗口实时发送运行状态
    exitSignal = pyqtSignal(str)

    def __init__(self, data):
        super().__init__()
        # 窗口传递的参数
        logger.info(f'程序运行参数为：{data}')

        # 任务类别
        self.task_type = data.get('task_type')

        # 任务名称（结果文件名称/样品名称）
        self.task_name = data.get('task_name')

        # 起始路径
        self.ori_path = data.get('ori_path')

        # 结果路径
        self.result_path = data.get('result_path')

        # 列表文件
        self.list_path = data.get('list_path')

        # 线程数
        self.thread_ = data.get('threads')

        """溯源与分子进化树"""
        # 序列文件
        self.xvlie_file = data.get('xvlie_file')
        # 序列信息
        self.xvlie_info = data.get('xvlie_info')
        # 新冠数据库
        self.database = data.get('database')

        """宏基因组特有参数"""
        # 模型文件
        self.model_file = data.get('model_name', '')
        # 纠错次数
        self.count = data.get('count', '')

        """新冠病毒序列拼接"""
        # dateset
        self.data_set = data.get('data_set')

        # 测序类型
        self.cexv_type = data.get('cexv_type', '')
        # meta
        self.meta = '-meta' if data.get('meta', '') else ''

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

    def weizhi_ctpj(self):
        """
        执行python文件中的命令
        未知病原-从头拼接
        :param sample: 样品名称
        :return:
        """
        try:
            thi_comm = f'python {exepath}/G_CONFIG/erdai/ngs_denove.py -raw_path {self.ori_path} -list_file {self.list_path} -result_path {self.result_path} -type {self.cexv_type} -threads {self.thread_} {self.meta}'
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
            # self.result = self.status + '：' + e.stderr
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            quit()

    def weizhi_xlfl(self):
        """
        执行python文件中的命令
        未知病原-序列分类
        :param sample: 样品名称
        :return:
        """
        try:
            thi_comm = f'python {exepath}/G_CONFIG/reads_classify.py -raw_path {self.ori_path} -list_file {self.list_path} -result_path {self.result_path} -type {self.cexv_type} -threads {self.thread_} '
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
            # self.result = self.status + '：' + e.stderr
            self.result = self.status + f'错误详情可查看：{exepath}/logs/task.log'
            self.exitSignal.emit(self.result)
            u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
            end_time = str(datetime.now()).split('.')[0]
            self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
            self.conn.commit()
            logger.error(f'{self.task_name} {self.status}：{e.stderr}')
            quit()

    def xinguan_suyuan(self):
        """
        新冠-溯源与分子进化树
        :param sample: 样品名称
        :return:
        """
        try:
            file_comm = f'python {exepath}/G_CONFIG/ncov_trace_tree.py -fasta_file {self.xvlie_file} -meta_file {self.xvlie_info} -result_path ' \
                        f'{self.result_path} -num_seqs {self.count} -db {self.database}'
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

    def xinguan_xlpj(self):
        """
        新冠-新冠病毒序列拼接
        :param sample: 样品名称
        :return:
        """
        try:
            file_comm = f'python {exepath}/G_CONFIG/erdai/ncov_illumina_assemble.py -raw_path {self.ori_path} -sample_lsit {self.list_path} ' \
                        f'-result_path {self.result_path} -dataset {self.data_set}'
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

    def xinguan_xlfx(self):
        """
        新冠-新冠病毒序列分析
        :param sample: 样品名称
        :return:
        """
        try:
            file_comm = f'python {exepath}/G_CONFIG/ncov_analyze.py -fasta_file {self.xvlie_file} -result_path {self.result_path}'
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

    def xinguan_wsfx(self):
        """
        新冠-新冠病毒序列分析
        :param sample: 样品名称
        :return:
        """
        try:
            file_comm = f'python {exepath}/G_CONFIG/erdai/ncov_sewage.py -rawdata {self.xvlie_file} -result  {self.result_path}'
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

    def liugan(self):
        """
        新冠-新冠病毒序列分析
        :param sample: 样品名称
        :return:
        """
        try:
            file_comm = f'python {exepath}/G_CONFIG/Flu_Virus/Flu_assemble.py -rawdata {self.xvlie_file} -result  {self.result_path}'
            logger.info(f'命令如下：{file_comm}')
            u_sql = 'update task set taskStatus=? where taskNm=? and taskType=?'
            # 将当前任务状态更新到数据库中，以便页面展示
            self.status = '正在运行'
            self.cursor.execute(u_sql, (self.status, self.task_name, self.task_type))
            self.conn.commit()
            self.exitSignal.emit(self.status)

            # thi_res = subprocess.run(file_comm, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            #                          universal_newlines=True, shell=True)
            # if thi_res.returncode == 0:
            #     logger.info('执行成功')
            #     logger.info(thi_res.stdout)
            # else:
            #     self.status = '执行失败！'
            #     logger.error(f'执行出错：{thi_res.stdout}')
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
        print(f'任务类型为：{self.task_type}')
        # self.get_path()
        self.insert_db()
        if self.task_type == '未知病原illumina测序数据分析-序列分类':
            self.weizhi_xlfl()
        elif self.task_type == '未知病原illumina测序数据分析-从头拼接':
            self.weizhi_ctpj()
        elif '溯源与分子进化树' in self.task_type:
            self.xinguan_suyuan()
        elif '新冠病毒序列拼接' in self.task_type:
            self.xinguan_xlpj()
        elif '新冠病毒序列分析' in self.task_type:
            self.xinguan_xlfx()
        elif '新冠病毒污水分析' in self.task_type:
            self.xinguan_wsfx()
        elif self.task_type == '流感病毒序列拼接':
            self.liugan()
        else:
            self.status = f'暂不支持该功能：{self.task_type}'

        self.status = '已完成' if '暂不支持' not in self.status else f'暂不支持该功能：{self.task_type}'
        self.exitSignal.emit(self.status)
        # # 程序运行结束后，更新数据库中任务信息
        u_sql = """update task set taskStatus=?, endTime=?, taskResult=? where taskNm=? and taskType=?"""
        end_time = str(datetime.now()).split('.')[0]
        self.cursor.execute(u_sql, (self.status, end_time, self.result, self.task_name, self.task_type))
        self.conn.commit()
        self.finish()

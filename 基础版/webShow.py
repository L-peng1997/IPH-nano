# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 19:50
# @Author  : Lvp
# @File    : webShow.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #引入Keys类包
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from G_COMM.runXinguan import logger
import os
from configparser import ConfigParser


base_path = os.getcwd()
config = ConfigParser()
config.read(f'{base_path}/G_CONFIG/config.ini', encoding='utf-8')


base_path = os.getcwd().replace('//', '/')


class WebShow(object):

    def __init__(self):
        self.url = 'https://clades.nextstrain.org/'
        # self.path_list = path_list
        # self.task_name = task_name
        self.N_list = []

    def get_file(self, path_list):
        """
        获取所选文件的内容
        :return:
        """
        data = []
        for path in path_list:
            with open(path, 'r') as f:
                file_con = f.read()
                data.append(file_con)
        result = ''.join(data)
        return result

    def get_result(self, path_list):
        self.opt = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(firefox_options=self.opt, executable_path=f'{base_path}/driver/geckodriver')
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(5)

        try:
            js1 = "document.getElementsByClassName('mx-auto btn-select-file btn btn-secondary')[0].click()"

            self.driver.execute_script(js1)

            # ActionChains(self.driver).move_by_offset(1000, 670).click().perform()

            js = 'var ucode = document.getElementById("sequence-input"); ucode.value=arguments[0]'

            file_con = self.get_file(path_list)
            # print(file_con)
            self.driver.execute_script(js, file_con)

            textarea = self.driver.find_element_by_id('sequence-input')
            textarea.send_keys(Keys.CONTROL, 'a')
            textarea.send_keys(Keys.CONTROL, 'x')
            textarea.send_keys(Keys.CONTROL, 'v')

            WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Run']")))
            time.sleep(1)
            btn2 = self.driver.find_element_by_xpath("//span[text()='Run']")
            btn2.click()

            # WebDriverWait(self.driver, 20, 1).until(
            #     EC.presence_of_element_located((By.XPATH, "//button[text()='Back']")))

            # time.sleep(10)

            # print(self.driver.window_handles)

        except Exception as e:
            print('selenium运行失败！！', e)
            logger.error(f'selenium运行失败,{e}')

    def open_weizhi(self):
        self.opt = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(firefox_options=self.opt, executable_path=f'{base_path}/driver/geckodriver')
        self.driver.maximize_window()
        url = config.get('Unknown_Path', 'result_url')
        try:
            self.driver.get(url)
            time.sleep(5)

            # self.driver.find_element_by_id("datafile-file_upload").send_keys(path)

        except Exception as e:
            print('selenium运行失败！！', e)
            logger.error(f'网页打开失败,{e}')


if __name__ == '__main__':

    path_list = ['D:/智源代码/高通量测序/file/高通量测序/4.mapping/NB21.consensus.fasta']
    a = WebShow()
    # a.get_result(path_list)
    a.open_weizhi()

# encoding utf-8
"""
@author: xiayu
@contact: xiayu_li@shannonai.com
@version: v0.0.1
@file: reg_exp.py
@time: 2019/1/5 12:45
@desc: 测试基础的正则表达式能力
一共三道题目
1、找出log中搜索最多的问题
2、找出log中搜索最多的时间段(精确到小时)
3、找出log中被问到的最多的银行的名称（推荐使用正则）
"""
import os
import json
import time
from tqdm import tqdm

# log存放的地址
data_path = '../data/osprey_response.log'

class LogAnalyzer(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def most_query(self):
        """
        找出log中搜索最多的问题
        implement here
        """
        raise NotImplementedError

    def most_query_time(self):
        """
        找出log中搜索最多的时间段
        implement here
        """
        times = []
        with open(self.file_path) as f_log:
            for line in tqdm(f_log.readlines()):
                log = json.loads(line)
                # print(log['ts'])
                times.append(time.localtime(log['ts']))
        print(len(times))

    def most_query_institution(self):
        """
        找出log中被问到的最多的银行的名称
        implement here
        """
        raise NotImplementedError

    def read_log_sample(self):
        """
        该函数为读取log中的问题和时间的样例
        :return:
        """
        with open(self.file_path) as f_log:
            lines = f_log.readlines()
            for line in lines:
                log = json.loads(line)
                # 这里的time是时间戳
                time = log['ts']
                print(time)
                # 问题的提取方式
                log_json = json.loads(log['json'])
                question = log_json['question']
                print(question)


def run():
    log_analyzer = LogAnalyzer(data_path)
    # log_analyzer.read_log_sample()
    # print(log_analyzer.most_query())
    print(log_analyzer.most_query_time())
    # print(log_analyzer.most_query_institution())


if __name__ == "__main__":
    run()


# encoding utf-8
"""
@author: xiayu
@contact: xiayu_li@shannonai.com
@version: v0.0.1
@file: reg_exp.py
@time: 2019/1/5 12:45
@desc: 测试基础的正则表达式能力
一共五道题目
1、匹配一个人的出生日期（1990年1月2日，1990.1.2， 1990.01.02，1990-01-02）
2、匹配身份证号或者护照号（一个数字或者大写英文，后面结若干数字，最后一个字符可以是英文也可以是数字）
3、匹配电子邮箱中‘@’前面的字符
4、文中出现的百分比（数字加百分号）
5、包含“股东和实际控制人”，但是不包含“承诺”
"""

# 测试数据存放的地址
import re

data_path = '../data/reg_exp.txt'

class Regexp(object):

    def __init__(self, file_path):
        with open(file_path) as f_e:
            self.lines = f_e.readlines()

    def search_birth_data(self, strs):
        """

        :param strs: 包含生日的string列表
        :return:
        """
        patterns = "\d{4}.*(年|-).*([0-9]|1[0-2]).*(月|-)\d{1,2}.*日?"
        for str in strs:
            if re.search(patterns, str):
                print(re.search(patterns, str).group())
    def search_identity_number(self, strs):
        """

        :param strs: 包含证件号码的string列表
        :return:
        """
        patterns = "\w+\d+\*+(\w{0,1}|\d{0,1})"
        for str in strs:
            if re.search(patterns, str):
                print(re.search(patterns, str).group())
    def search_email(self, strs):
        """

        :param strs: 包含电子邮箱的string列表
        :return:
        """
        patterns = "[a-zA-Z].*(?=@)"
        for str in strs:
            if re.search(patterns, str):
                print(re.search(patterns, str).group())

    def search_percentage(self, strs):
        """

        :param strs: 包含百分比的string列表
        :return:
        """
        patterns = "\d+\.\d+%"
        for str in strs:
            if re.search(patterns, str):
                print(re.search(patterns, str).group())

    def search_share_holder(self, strs):
        """

        :param strs: 包含股东的string列表
        :return:
        """
        patterns = "股东和实际控制人"
        patterns2 = "承诺"
        for str in strs:
            if re.search(patterns,str):
                if not re.search(patterns2,str):
                    print(str)

def run():
    regexp = Regexp(data_path)
    regexp.search_birth_data(regexp.lines[:3])
    regexp.search_identity_number(regexp.lines[3:5])
    regexp.search_email(regexp.lines[5:7])
    regexp.search_percentage(regexp.lines[7:8])
    regexp.search_share_holder(regexp.lines[8:])


if __name__ == '__main__':
    run()
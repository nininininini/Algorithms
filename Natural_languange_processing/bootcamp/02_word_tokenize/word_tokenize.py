# coding: utf-8
"""
@author: gladuo
@contact: me@gladuo.com

@version: 1.0
@file: word_tokenize.py
@time: 2019-03-09 10:30

这一行开始写关于本文件的说明与解释
"""

from typing import List


class Tokenizer(object):
    def word_tokenize(self, sequence: str) -> List[str]:
        raise NotImplementedError


def run():
    tokenizer = Tokenizer()
    print(tokenizer.word_tokenize('欢迎加入香侬科技！'))


if __name__ == '__main__':
    run()

"""
搜索引擎搭建
"""

from typing import List

class Indexer(object):
    def build_index(self, document_list: List[str]):
        """
        给定document list建立索引
        :param document_list:
        :return:
        """
        raise NotImplementedError

class Searcher(object):
    def load_index(self, index_path: str):
        """
        将index载入内存
        :param index_path:
        :return:
        """
        raise NotImplementedError
    def search(self, query: str):
        """
        输入一个query，返回10个最相关的结果
        :param query:
        :return:
        """
        raise NotImplementedError
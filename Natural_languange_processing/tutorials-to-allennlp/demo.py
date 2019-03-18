# _*_ encoding: utf-8 _*_
"""
@file: demo.py
@author: kebo
@contact: itachi971009@gmail.com
@time: 2019-03-18 15:09
@desc:
"""
## read readme.md
import os
if __name__ == "__main__":
    os.system(" allennlp train tests/academic_paper_classifier.json -s tests/output_dir  "
              "--include-package my_library")
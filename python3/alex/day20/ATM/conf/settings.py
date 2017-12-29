# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/25

import os,sys,logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': '%s\\db' %BASE_DIR
}

LOG_LEVEL = logging.INFO
LOG_TYPE = {
    "transcation": "transcations.log",
    "access": "access.log",
}
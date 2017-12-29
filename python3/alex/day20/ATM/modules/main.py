# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/25

import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from modules import accounts,auth,db_handler,logger,transaction

trans_logger  = logger.logger('transaction')
access_logger = logger.logger('access')

user_data = {
    "authenticated": False,
    "user_id": None,
    "user_data": None
}


def interactive(acc_data):
    

def run():
    acc_data = auth.login(user_data,access_logger)
    if user_data["authenticated"]:
        user_data["user_id"] = acc_data





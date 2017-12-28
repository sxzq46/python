# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/25

import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from modules import accounts,auth,db_handler,logger,transaction

user_account = {
    "authenticated": False,
    "user_id": None,
    "user_data": None
}


user_data = auth

if user_account["authenticated"]:
    user_data = user_account["user_id"]




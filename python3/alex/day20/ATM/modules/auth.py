# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/26

from modules import db_handler
from modules import logger
from conf import settings
import json
import time


def auth(account,password):
    data = db_handler.db_handler_api(account,password)
    exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
    if time.time() > exp_time_stamp:
        print("Account [%s] has expired,Plz get a new card!" %account)
    else:
        return data


def login(user_data,log_obj):
    retry_count = 0
    while user_data['authenticated'] is False and retry_count < 3:
        account = input("Account:")
        password = input("PassWord:")
        account_data = auth(account,password)
        if account_data:
            user_data['authenticated'] = True
            user_data['user_id'] = account
            return account_data
        retry_count += 1
    else:
        log_obj.error("Account [%s] too many login attempts" % account)

# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/12/26

from modules import db_handler
from modules import logger
from conf import settings
import json
import time


def auth(account,password):
    pass


def login(user_data):
    retry_count = 0
    while user_data['authenticated'] is False and retry_count < 3:
        account = input("Account:")
        password = input("PassWord:")
        account_data = auth(account,password)
        if account_data:
            pass

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

def account_info(acc_data):
    pass

def repay(acc_data):
    pass

def withdraw(acc_data):
    pass

def transfer(acc_data):
    pass

def pay_check(acc_data):
    pass

def logout(acc_data):
    pass


def interactive(acc_data):
    menu = u'''
    1. 账户信息
    2. 还款
    3. 取款
    4. 转账
    5. 账单
    6. 退出
    '''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            print('acc_data',acc_data)
            menu_dic[user_option](acc_data)
        else:
            print("Option does not exist!")

def run():
    acc_data = auth.login(user_data,access_logger)
    if user_data["authenticated"]:
        user_data["user_id"] = acc_data





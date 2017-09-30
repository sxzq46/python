#__author: XiangzhongShi
#date: 2017/8/11
#-*- coding:utf-8 -*-


import cx_Oracle

def select_quotabid(code):
    conn = cx_Oracle.connect('quotabid/quotabid_may5@172.30.32.159:1521/biddb')
    cr2 = conn.cursor()
    sql2 = "SELECT bid_app_code,bid_code,bid_contract_no,bid_state FROM quotabid.qb_bid_info WHERE bid_app_code IN (%s) and bid_state not in('BS_WHB','BS_YHB')" %(code,)
    cr2.execute(sql2)
    rs2 = cr2.fetchall()
    cr2.close()
    conn.close()
    if rs2:
        print("降额申请进件，没有取消挂标状态！")
        print(rs2)
        return str(rs2)

if __name__ == "__main__":
    select_quotabid()
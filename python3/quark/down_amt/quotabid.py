#__author: XiangzhongShi
#date: 2017/8/10

import cx_Oracle

def quotabid_sql(code):
    quotabid_conn = cx_Oracle.connect('quotabid/quotabid_may5@172.30.32.159:1521/biddb')
    quotbid_cr = quotabid_conn.cursor()
    print("====标的系统降额脚本处理====")
    bid_app_code = code
    sql1 = "DELETE FROM quotabid.qb_bid_info WHERE bid_app_code IN (%s);\n" % (bid_app_code,) + "\r"
    sql2 = "DELETE FROM quotabid.qb_bid_detail_info WHERE bid_code IN (SELECT bid_code FROM quotabid.qb_bid_info WHERE bid_app_code IN (%s));" % (bid_app_code,) + "\r\r"
    sql3 = "DELETE FROM quotabid.qb_bid_config WHERE bid_app_code in(%s);" % (bid_app_code,) + "\r"
    quotabid_content = "--quotabid用户执行--\n" + "--删除标的数据，重新审核！--\n" + sql2 + sql1 + sql3
    quotabid_conn.close()
    return quotabid_content



if __name__ == "__main__":
    quotabid_sql()
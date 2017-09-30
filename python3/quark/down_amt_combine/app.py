#__author: XiangzhongShi
#date: 2017/8/10

import cx_Oracle

def app_sql(code,staff_info):
    app_conn = cx_Oracle.connect('appread/appread_2016@172.30.30.60:1521/COREPRD.quark.com')
    app_cr = app_conn.cursor()
    app_code = code
    check_sql = "SELECT id FROM app.app_main WHERE app_code in(%s)"  % (app_code,)
    app_cr.execute(check_sql)
    exist_id = app_cr.fetchall()
    if exist_id:
        print("====审核系统降额脚本处理====")
        sql1 = "DELETE FROM qcreditadm.app_queue_log WHERE app_id IN (SELECT id FROM app.app_main WHERE app_code in(%s)) AND status_order > '140';" % (
        app_code,) + "\r\r"
        sql2_1 = "UPDATE app.app_queue SET is_reset = 'Y',app_status = 'FAPPRDISPED',thd_deal_status = '',thd_app_code = '',status_phase='PHASE_APPR',do_action='sysRTDisp',is_final='N',status_order=140%s WHERE app_code IN (%s);" % (
        staff_info,app_code) + "\r\r"
        sql2_2 = "UPDATE app.app_main SET app_status='FAPPRDISPED' where app_code in(%s);" % (app_code,) + "\r\r"
        sql2_3 = "UPDATE app.app_dcout SET dcout_is_final='N', dcout_final_decision = '' WHERE app_id  IN (SELECT id FROM app.app_main WHERE app_code IN (%s));" % (
        app_code,) + "\r\r"
        sql2_4 = "UPDATE app.app_dcin SET dcin_decision_code = '', dcin_action = 'sysRTDisp', dcin_manual_Decision = '' WHERE app_id  IN (SELECT id FROM app.app_main WHERE app_code IN (%s));" % (
        app_code,) + "\r\r"
        sql3 = "DELETE FROM app.qc_bd_changes_his WHERE main_app_code IN (%s);" % (app_code,) + "\r"
        app_content = "--qcreditadm用户执行--\n" + "--等待终审-删除log--\n" + sql1 + "--app用户执行--\n" + "--等待终审-无指定--\n" + sql2_1 + sql2_2 + sql2_3 + sql2_4 + "--删除同步历史--\n" + sql3
    else:
        app_content = ""
    app_conn.close()
    return app_content
if __name__ == "__main__":
    app_sql()
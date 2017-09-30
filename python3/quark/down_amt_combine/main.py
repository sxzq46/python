#__author: XiangzhongShi
#date: 2017/8/10

import app
import app_state
import quotabid
import quotabid_state
import quotabid_WHB
import mail

itop_id = input("请输入ITOP编号及标题：")
code = input("请输入进件号，格式为：'170707002009010004','170707002009010003' :")
mailto_list = ['xiangzhongshi@quarkfinance.com']
staff = input("降额操作如需指定审核人员请输入1，不填或输入其他则正常执行：")
if staff == 1:
    staff_info = ",is_final_lock='Y',DECISION_NO_FINAL='xiaoyonghong',approve_name='洪小勇'"
else:
    staff_info = ""

while True:
    method_code = input("请选择操作编号：1.降额操作，2.查看降额状态，3.取消挂标：")
    if method_code.isdigit():
        method_code = int(method_code)
        if method_code == 1:
            mail_head = "降额申请"
            if app.app_sql(code,staff_info):
                print(app.app_sql(code))
                # mail.send_mail(itop_id, mailto_list, "降额申请-审核", app.app_sql(code),)
            if quotabid.quotabid_sql(code):
                print(quotabid.quotabid_sql(code))
                # mail.send_mail(itop_id, mailto_list, "降额申请-标的", quotabid.quotabid_sql(code))
            break
        elif method_code == 2:
            mail_head = "降额申请状态"
            if app_state.select_app(code):
                app_state.select_app(code)
                # mail.send_mail(itop_id, mailto_list, "降额申请-审核状态", app.select_app(into_code))
            if quotabid_state.select_quotabid(code):
                quotabid_state.select_quotabid(code)
                # mail.send_mail(itop_id, mailto_list, "降额申请-标的状态", quotabid.select_quotabid(into_code))
            break
        elif method_code == 3:
            mail_head = "取消挂标"
            if quotabid_WHB.select_WHB(code):
                quotabid_WHB.select_WHB(code)
            break
        else:
            print('请输入正确操作编号！')
    else:
        print('请输入正确操作编号！')

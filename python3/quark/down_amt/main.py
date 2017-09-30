#__author: XiangzhongShi
#date: 2017/8/10

import app
import quotabid
import mail

itop_id = input("请输入ITOP编号及标题：")
code = input("请输入进件编号：")
mailto_list = ['xiangzhongshi@quarkfinance.com']

print(app.app_sql(code))
print(quotabid.quotabid_sql(code))

mail.send_mail(itop_id, mailto_list, "降额申请-审核", app.app_sql(code))
mail.send_mail(itop_id, mailto_list, "降额申请-标的", quotabid.quotabid_sql(code))
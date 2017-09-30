#__author: XiangzhongShi
#date: 2017/8/9


import time
import datetime
import stomp

begin = datetime.datetime.now()

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, body):
        print(body)
    def on_before_message(self, headers, body):
        print(body)

conn = stomp.Connection([('172.29.150.204',61613)])
conn.set_listener('My',MyListener())
conn.start()
# conn.connect(headers={'client-id':'001'})
conn.connect()
# conn.subscribe(destination='/topic/test',id=1,ack='auto',headers={'activemq.subscriptionName':'sxz'})
conn.subscribe(destination='/queue/test10',id=1,ack='auto')
end = datetime.datetime.now()
time.sleep(30)
conn.disconnect()

print(end-begin)

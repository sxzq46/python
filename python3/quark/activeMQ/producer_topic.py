#__author: XiangzhongShi
#date: 2017/8/9

import time
import datetime
import stomp
i = 0

begin = datetime.datetime.now()
conn = stomp.Connection([('172.29.150.202',61613)])
conn.start()
conn.connect()
while i < 1000:
    # conn.send(body='fuck!!!!!', destination='/topic/test', headers={'type': 'textMessage', 'persistent': 'true'})
    conn.send(body='fuck!!!!!', destination='/queue/test4', headers={'type': 'textMessage', 'persistent': 'true'})
    # conn.send(body='fuck!!!!!', destination='/queue/test', headers={'type': 'textMessage'})
    i = i+1
time.sleep(1)
conn.disconnect()
end = datetime.datetime.now()

print(end-begin)
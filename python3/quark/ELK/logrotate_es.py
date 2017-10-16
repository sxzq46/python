# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/20


import requests,time,json,datetime

project_index= ["cfca","cmf","epay","goapi","jytloan","payment","tts"]

def index_get(url):
    session = requests.get(url)
    session_info = json.dumps(session.json(),sort_keys=True, indent=4, separators=(',', ': '))
    session_format = eval(session_info)
    return session_format

def index_del(index):
    for i in index:
        es_create_time = int(index[i]['settings']['index']['creation_date']) // 1000
        current_time = time.mktime(time.strptime(str(datetime.date.today()), '%Y-%m-%d'))
        diff_time = (current_time - es_create_time) // (3600 * 24)
        if diff_time > 10:
            session2 =  "http://172.29.150.198:9200/%s" %(i)
            print(session2)
            # requests.delete(session2)

if __name__ == "__main__":
    for i in project_index:
        purl = "http://172.29.150.198:9200/%s-*" %(i)
        es_index = index_get(purl)
        index_del(es_index)



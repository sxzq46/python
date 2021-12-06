# -*- coding: utf-8 -*-
# __author: XiangzhongShi
# date: 2021/2/2

import requests
import time
import json
import datetime

project_indices = ["prod-log4j", "prod-ink8s", "logstash-prod", "prod-mysql", "prod-tomcat"]
forcemerge_days = 4
es_urls = ["http://10.224.14.161:9200", "http://10.224.14.162:9200", "http://10.224.14.163:9200"]
es_user = "elastic"
es_passwd = "tD6$wC0`mB2|cC0&cC"

# es地址高可用
for es_url in es_urls:
    try:
        session = requests.get(es_url, auth=(es_user, es_passwd), timeout=3)
        if session.status_code == 200:
            es_url = es_url
            break
    except requests.exceptions.ConnectionError:
        print('connect Failed', es_url)


# 获取所有index
def indices_get(url):
    session = requests.get(url, auth=(es_user, es_passwd))
    session_info = json.dumps(session.json(),
                              sort_keys=True,
                              indent=4,
                              separators=(',', ':'))

    # print(session_info)
    session_format = json.loads(session_info)
    # print(session_format)
    return session_format


# 删除过期index
def indices_forcemerge(indices):
    for i in indices:
        # print(i)
        es_create_time = int(
            indices[i]['settings']['index']['creation_date']) // 1000
        current_time = time.mktime(
            time.strptime(str(datetime.date.today()), '%Y-%m-%d'))
        diff_time = (current_time - es_create_time) // (3600 * 24)
        if diff_time > forcemerge_days:
            session_post_url = "%s/%s/_forcemerge?max_num_segments=1" % (es_url, i)
            session_get_url = "%s/_cat/segments/%s?v&h=segment" % (es_url, i)
            print(datetime.datetime.now(), "start forcemerge: ", session_post_url)

            while True:
                try:
                    session_len = requests.get(session_get_url, auth=(es_user, es_passwd))
                    if len(session_len.text.splitlines()) <= 4:
                        print("done")
                        break
                    else:
                        requests.post(session_post_url, auth=(es_user, es_passwd), timeout=300)
                except requests.exceptions.RequestException:
                    time.sleep(5)


if __name__ == "__main__":
    for i in project_indices:
        purl = "%s/%s-*" %(es_url, i)
        es_indices = indices_get(purl)
        indices_forcemerge(es_indices)

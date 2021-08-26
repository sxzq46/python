# -*- coding: utf-8 -*-
# __author: XiangzhongShi
# date: 2021/2/2

import requests
import time
import json
import datetime

project_indices = ["prod-log4j", "prod-ink8s", "logstash-prod", "prod-mysql", "prod-tomcat"]
del_days = 29
es_urls = ["http://10.224.14.153:9200", "http://10.224.14.152:9200", "http://10.224.14.154:9200"]
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


# 针对index做snapshot
def indices_snapshot(indices, prefix):
    snapshot_indices = []
    for i in indices:
        es_create_time = int(
            indices[i]['settings']['index']['creation_date']) // 1000
        current_time = time.mktime(
            time.strptime(str(datetime.date.today()), '%Y-%m-%d'))
        diff_time = (current_time - es_create_time) // (3600 * 24)
        if diff_time > del_days:
            snapshot_indices.append(i)
    if snapshot_indices:
        snapshot_indices_str = ','.join(snapshot_indices)
        snapshot_json = {
            "indices": snapshot_indices_str,
            "ignore_unavailable": True,
            "include_global_state": False,
            "metadata": {
                "taken_by": "py_scripts",
                "taken_because": "backup before delete"
            }
        }
        headers = {
            'Content-Type': 'application/json'
        }
        snapshot_date = time.strftime("%Y-%m-%d")
        snapshot_url = "%s/_snapshot/indices-backup/%s_%s?wait_for_completion=true" % (es_url, prefix, snapshot_date)
        requests.put(snapshot_url, auth=(es_user, es_passwd), headers=headers, data=json.dumps(snapshot_json))
        # print("===snapshot===")
        # print(snapshot_json)
        # print(snapshot_url)


# 删除过期index
def indices_del(indices):
    for i in indices:
        # print(i)
        es_create_time = int(
            indices[i]['settings']['index']['creation_date']) // 1000
        current_time = time.mktime(
            time.strptime(str(datetime.date.today()), '%Y-%m-%d'))
        diff_time = (current_time - es_create_time) // (3600 * 24)
        if diff_time > del_days:
            session2 = "%s/%s" % (es_url, i)
            # print("===del===")
            # print(session2)
            requests.delete(session2, auth=(es_user, es_passwd))


if __name__ == "__main__":
    for i in project_indices:
        purl = "%s/%s-*" %(es_url, i)
        es_indices = indices_get(purl)
        indices_snapshot(es_indices, i)
        indices_del(es_indices)

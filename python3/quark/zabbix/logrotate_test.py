# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/15


import sys,os,requests,time,re,json

hostname = 'BGP-NETAM-01'
log_path = '/usr/apache-tomcat-7.0.69/bin/logs'
bak_path_ = '/home/logger/log_bak'
save_days = '20'

def handle(hostname,log_path,bak_path_,save_days):
    resp = session.post('http://172.30.33.183:7991', json=[{
        'client': 'local',
        'tgt': hostname,
        'fun': 'state.sls',
        'arg': ['ifconfig'],
        'kwarg': {"pillar":{"log_path":log_path,"bak_path_":bak_path_,"save_days":save_days}},
    }])
    return json.dumps(resp.json())

if __name__ == "__main__":
    session = requests.Session()
    session.post('http://172.30.33.183:7991/login', json={
        'username': 'Lsaltapiuser',
        'password': '&87YuApi$',
        'eauth': 'pam',
    })
    a = handle(hostname=hostname, log_path=log_path, bak_path_=bak_path_, save_days=save_days)
    print(a)
    m = re.search("is running as PID", a)
    print(m)
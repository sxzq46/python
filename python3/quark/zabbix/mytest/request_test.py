# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2017/9/19


import sys,os,requests,time,re,json


session = requests.get('http://172.16.35.87:8000/login', json={
    'username': 'shixz',
    'password': 'shixz',
    'eauth': 'pam'
})

print(session)

session2 = requests.get('http://172.30.33.183:7991/login', json={
    'username': 'Lsaltapiuser',
    'password': '&87YuApi$',
    'eauth': 'pam',
})

print(session2)
# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/15


from wsgiref.simple_server import make_server

def application(environ, start_response):
    #通过environ封装成一个所遇请求信息的对象
    #start_response可以很方便地设置响应头
    start_response('200 ok',[('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

#封装socket对象以及准备过程(socket,bind,listen)
httpd = make_server('',8080,application)

print('Serving HTTP on port 8000...')
#开始监听HTTP请求
httpd.serve_forever()
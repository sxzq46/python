# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/15


from wsgiref.simple_server import make_server
import time





def application(environ, start_response):
    # print('environ',environ['PATH_INFO'])
    start_response('200 ok', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']
    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)


#封装socket对象以及准备过程(socket,bind,listen)
httpd = make_server('',8080,application)

print('Serving HTTP on port 8080...')
#开始监听HTTP请求
httpd.serve_forever()
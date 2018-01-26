# -*- coding: utf-8 -*-
#__author: XiangzhongShi
#date: 2018/1/15


from controllers import current_time

def routers():
    urlpatterns = (
        ('/current_time',current_time),
    )


    return  urlpatterns
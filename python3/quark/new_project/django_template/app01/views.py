from django.shortcuts import render,HttpResponse
import datetime

# Create your views here.

def index(req):
    class Person:
        def __init__(self,name,age):
            self.name=name
            self.age=age

    s="hello"
    s2=[1,22,333]
    s3={'username':'alex','sex':'male'}
    s4=datetime.datetime.now()
    s5=Person("yuan",18)
    s6=6
    s7=[123,234]
    s8="<a herf='#'>跳转</a>"
    return render(req,"index.html",{"obj":s8})

def login(req):
    if req.method == "POST":
        return HttpResponse("ok")
    name="hello"
    num=66
    return render(req,"login.html",locals())


def ordered(req):

    return render(req,"ordered.html")

def shopping_car(req):

    return render(req,"shopping_car.html")
from django.shortcuts import render,redirect,HttpResponse
import datetime

# Create your views here.


def login(request):
    print("COOKIES",request.COOKIES)
    print("SESSION",request.session)

    if request.method=="POST":
        name = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if name == "shixz" and pwd == "123":

            # ret = redirect("/index/")
            # ret.set_cookie("username",{"11":"22"},max_age=10,expires=datetime.datetime.utcnow()+datetime.timedelta(days=3))
            # return ret

            # COOKIE SESSION
            request.session["is_login"] = True
            request.session["user"] = name
            return redirect("/index/")

    return render(request,"login.html")

def index(request):

    # if request.COOKIES.get("username",None):
    #     name = request.COOKIES.get("username",None)
    #     return render(request,"index.html",locals())

    if request.session.get("is_login",None):
        name = request.session.get("user",None)
        return render(request,"index.html",locals())

    else:
        return redirect("/login/")


def fbv(request):

    if request.method == "GET":
        return HttpResponse("FBV.GET")
    elif request.method == "POST":
        return HttpResponse("FBV.POST")

from django.views import View
class cbv(View):
    def get(self,request):
        # 根据请求头中的request method进行自动执行
        return render(request,"cbv.html")
        #return HttpResponse("CBV.GET")
    def post(self,request):
        return HttpResponse("CBV.POST")
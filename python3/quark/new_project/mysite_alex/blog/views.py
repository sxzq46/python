from django.shortcuts import render,HttpResponse,render_to_response,redirect
import datetime
from blog import models
# Create your views here.

def cur_time(request):
    times = datetime.datetime.now()
    return render(request,"cur_time.html",{"abc":times})



def userInfo(req):
    if req.method == "POST":
        u = req.POST.get("username",None)
        g = req.POST.get("gender",None)
        e = req.POST.get("email",None)
        # user = {"username":username,"gender":gender,"email":email}
        models.UserInfo.objects.create(
            username = u,
            gender = g,
            email = e,
        )
    user_list = models.UserInfo.objects.all()
    return render(req, "index.html",{"user_list":user_list})

def index(req):
    print("req.GET",req.GET)
    if req.method == "POST":
        username = req.POST.get("username")
        pwd = req.POST.get("pwd")
        if username == "alex" and pwd == "123":
            return HttpResponse("登陆成功！")
    # return render(req,"login.html")
    alex = "shixz"
    eric = "adasd"
    return render_to_response("new.html",locals())

def introduce(req):
    return HttpResponse("ok")

def login(req):
    if req.method=="POST":
        if 1:
            return redirect("/home/")
    return render(req,"login.html")

def home(req):
    name = "洗澡"
    return render(req,"home.html", {"name":name})
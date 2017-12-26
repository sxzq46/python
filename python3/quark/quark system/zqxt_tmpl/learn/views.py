from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    string = "这只是个测试。"
    testlist = ["HTML","CSS","JQuery","Python","Django"]
    info_dict = {'site':'quark','content':'系统'}
    # longlist = map(str,range(10))
    longlist = []
    return render(request,'home.html',{'string':string,'testlist':testlist,'info_dict':info_dict,'longlist':longlist})

def add(request,a ,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))



from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

# def index(request):
#     return HttpResponse("欢迎光临，夸克金融！")

# def index(request):
#     return render(request, 'home.html')

# def home(request):
#     string = "quark金融"
#     return render(request, 'home.html',{'string':string})

# def home(request):
#     tList = ["html", "css", "python", "django"]
#     return render(request, 'home.html', {'tList':tList})

def home(request):
    List = map(str, range(100))
    return render(request, 'home.html', {'List': List})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def  old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2',args=(a, b))
    )
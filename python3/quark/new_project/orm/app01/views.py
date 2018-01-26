from django.shortcuts import render,HttpResponse
from app01.models import *
# Create your views here.


def index(request):

    return render(request,"index.html")

def addbook(request):

    # b = book(name="python基础",price=99,author="shixz",pub_date="2018-01-25")
    # b.save()
    book.objects.create(name="老男孩linux",price=67,author="oldboy",pub_date="2018-01-26")

    return HttpResponse("添加成功")

def update(request):

    # book.objects.filter(author="shixz").update(price=999)
    # b = book.objects.get(author="oldboy")
    # b.price = 111
    # b.save()
    return HttpResponse("修改成功！")

def delete(request):

    book.objects.filter(author="oldboy").delete()
    return HttpResponse("删除成功！")

def select(request):
    book_list = book.objects.filter(id=2)
    book_list = book.objects.all()[:3]
    book_list = book.objects.all()[::-1]
    book_list = book.objects.first()
    book_list = book.objects.last()
    book_list = book.objects.get(id=2)  #只能取出一条记录时不报错
    ret = book.objects.filter(author="shixz").values("name","price")
    ret2 = book.objects.filter(author="shixz").values_list("name","price")
    ret2 = book.objects.exclude(author="shixz").values("name","price")
    print(ret)
    print(ret2)
    book_list = book.objects.all().values("author").distinct()
    book_count = book.objects.all().values("author").distinct().count()
    print(book_count)
    book_list = book.objects.filter(price__gt=100).values("name","price")

    return render(request,"index.html",{"book_list":book_list})
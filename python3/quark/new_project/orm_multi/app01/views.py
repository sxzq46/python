from django.shortcuts import render,HttpResponse
from django.db.models import Avg,Min,Sum,Max,Count,F,Q

# Create your views here.
from app01.models import *

def index(request):

    return render(request,"index.html")

def addbook(request):
    # Book.objects.create(name="linux运维",price=77,pub_date="2018-01-02",publish_id=2)
    publish_obj = Publish.objects.filter(name="人民出版社")[0]
    Book.objects.create(name="GO", price=77, pub_date="2018-01-02", publish=publish_obj)
    return HttpResponse("添加成功")

def update():pass
def select(request):

    # 一对多：book_obj.publish-------一定是一个对象
    # book_obj = Book.objects.get(name="python")
    # print(type(book_obj))
    # print(book_obj.publish.name)
    # print(book_obj.publish.city)
    # print(type(book_obj.publish))

    # 查询人民出版社出过的所有书籍名字和价格
    # 方式一：
    # pub_obj = Publish.objects.filter(name="人民出版社")[0]
    # ret = Book.objects.filter(publish=pub_obj).values("name","price")
    # print(ret)

    # 方式二：
    # pub_obj = Publish.objects.filter(name="人民出版社")[0]
    # print(pub_obj.book_set.all().values("name","price"))
    # print(type(pub_obj.book_set.all()))

    # 方式三
    # ret = Book.objects.filter(publish__name="人民出版社").values("name","price")
    # print(ret)

    #python出版社的名字
    # ret2 = Publish.objects.filter(book__name="python").values("name")
    # print(ret2)
    #
    # ret3 = Book.objects.filter(name="python").values("publish__name")
    # print(ret3)
    #
    # ret4 = Book.objects.filter(publish__city="北京").values("name")
    # print(ret4)
    #
    # ret5 = Book.objects.filter(pub_date__lt="2018-01-23",pub_date__gt="2018-01-14").values("publish__name")
    # print(ret5)

    # 通过对象的方式绑定关系
    # book_obj = Book.objects.get(id=3)
    # print(book_obj.authors.all())
    # print(type(book_obj.authors.all()))
    #
    # author_obj = Author.objects.get(id=2)
    # print(author_obj.book_set.all())

    # book_obj = Book.objects.get(id=4)
    # author_objs = Author.objects.all()
    # book_obj.authors.add(*author_objs)
    # book_obj.authors.remove(1)

    # 创建第三张表，此方法比较麻烦，不建议使用
    # Book_Author.objects.create(book_id=2,author_id=3)
    # obj = Book.objects.get(id=2)
    # print(obj.book_author_set.all()[0].author)

    # shixz出过的书籍名称及价格
    # ret = Book.objects.filter(book_author__author__name="shixz").values("name","price")
    # print(ret)

    # ret2 = Book.objects.filter(authors__name="shixz").values("name","price")
    # print(ret2)

    # ret = Book.objects.all().aggregate(Avg("price"))
    # ret = Book.objects.all().aggregate(Sum("price"))
    # ret = Book.objects.filter(authors__name="shixz").aggregate(shixz_money=Sum("price"))
    # ret = Book.objects.filter(authors__name="shixz").aggregate(shixz_money=Count("price"))
    # ret = Book.objects.values("authors__name").annotate(Sum("price"))
    # ret = Publish.objects.values("name").annotate(Min("book__price"))
    # ret = Book.objects.get(name="GO",price=77)
    # print(ret)
    # Book.objects.all().update(price=F("price")+10)
    # ret = Book.objects.filter(Q(price=87)&~Q(name="GO"))
    ret = Book.objects.filter(Q(name__contains="G"))
    print(ret)


    return HttpResponse("查询成功")

def delete():pass

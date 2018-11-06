from datetime import date

from django.shortcuts import render, redirect
from booktest.models import BookInfo


# Create your views here.
# 查询所有图书并显示
def index(request):
    # list = BookInfo.objects.all()
    # list = BookInfo.objects.filter(id__exact=1)
    list = BookInfo.objects.filter(id=1)
    return render(request, "booktest/index.html", {"list":list})


# 创建新图书
def create(request):
    book = BookInfo()
    book.btitle = "流星蝴蝶剑"
    book.bpub_date = date(1995, 12, 30)
    book.save()
    # 转向到首页
    return redirect("/")


# 逻辑删除指定编号的图书
def delete(request, id):
    book = BookInfo.objects.get(id=int(id))
    book.delete()
    # 转向到首页
    return redirect("/")

import json

from django.http import HttpResponse
from django.shortcuts import render

from django_bootstrap_table_web.models import User


# Create your views here.

def index(request):
    data = {
        "name": "hello",
        "sex": "男",
    }

    return render(request, 'user.html', data)


from django_bootstrap_table_web.models import user2dict


def detail(request):
    u = user2dict(User.objects.get(id=int(request.GET.get("id"))))
    return HttpResponse(json.dumps(u), content_type="application/json")


# 返回user json数据
def user_list(request):
    limit, offset = [None, None]
    if "limit" in request.GET:
        limit = request.GET["limit"]
    if "offset" in request.GET:
        offset = request.GET["offset"]
    print("limit:{},offset:{}".format(limit, offset))
    users = User.objects.all()
    rows = []
    for user in users:
        rows.append(user2dict(user))
    data = {
        "total": User.objects.count(),
        "rows": rows
    }
    print("data:", data)
    return HttpResponse(json.dumps(data), content_type="application/json")


def newdata(request):
    data = {
        "newcount": User.objects.count(),
        "username": "admin"
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def datacount(request):
    data = {
        "d": 10,
        "c": ["2018-02-04"]
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def hello(request):
    print("aaa")
    return HttpResponse("hello world!")

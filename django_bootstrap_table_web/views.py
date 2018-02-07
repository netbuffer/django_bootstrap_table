import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django_bootstrap_table_web.models import User
from django_bootstrap_table_web.models import user2dict


# Create your views here.

def index(request):
    data = {
        "name": "hello",
        "sex": "男",
    }
    return render(request, 'user.html', data)


# 用户详情
def detail(request, id=None):
    if not id:
        if not request.GET.get("id"):
            id = None
        else:
            id = request.GET.get("id")
    pass
    u = None
    try:
        u = user2dict(User.objects.get(id=id))
    except Exception as err:
        print("err:", err)
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

# redirect响应
def redirect(request):
    return HttpResponseRedirect(reverse("django_bootstrap_table:detail", args=(1,)))

import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django_bootstrap_table_web.models import User
from django_bootstrap_table_web.models import user2dict
from .forms import UserForm
from .apps import DjangoBootstrapTableWebConfig

# Create your views here.

USER_TABLE_SUFFIX = "_user"


# 添加/修改用户
def user(request):
    if request.method == "GET":
        user_id = request.GET.get('id')
        if user_id and int(user_id) > 0:
            user_id = int(user_id)
            user_form = UserForm(instance=User.objects.get(pk=user_id))
        else:
            user_form = UserForm()
        return render(request, "user/add.html", {"user_form": user_form, "user_id": user_id})
    elif request.method == "POST":
        user_id = request.POST.get("id", 0)
        if user_id and int(user_id) > 0:
            user_id = int(user_id)
            message = "修改成功"
            form = UserForm(request.POST, instance=User.objects.get(pk=user_id))
        else:
            message = "添加成功"
            form = UserForm(request.POST)
        if form.is_valid():
            is_save = True
        if is_save:
            form.save()
        else:
            print("error:", form.errors)
            message = form.errors
        return render(request, "user/add.html", {"message": message, "user_id": user_id})
    else:
        pass


# 删除用户
def delete_user(request):
    data = {
        "success": True,
    }
    user_id = request.GET.get("id", None)
    if user_id and int(user_id) > 0:
        try:
            User.objects.get(pk=user_id).delete()
        except Exception as err:
            data["err"] = err
            data["success"] = False
    return JsonResponse(data)


# 用户详情
def detail(request, id=None):
    if id:
        user_id = id
    else:
        user_id = request.GET.get("id", None)
    if not user_id:
        return JsonResponse([])
    try:
        return JsonResponse(user2dict(User.objects.get(id=user_id)))
    except Exception as err:
        print("err:", err)
        return JsonResponse([], safe=False)


# 返回user list json数据
def user_list(request):
    limit, offset = [None, None]
    if "limit" in request.GET:
        limit = request.GET["limit"]
    if "offset" in request.GET:
        offset = request.GET["offset"]

    order = request.GET.get("order", default="desc")
    order = "-" if order == "desc" else ""
    sort = request.GET.get("sort", default="adddate")
    if limit and int(limit) > 0 and offset and int(offset) >= 0:
        users = User.objects.order_by(order + sort).all()[int(offset):int(offset) + int(limit)]
    else:
        users = User.objects.order_by(order + sort).all()

    rows = []
    for user in users:
        rows.append(user2dict(user))
    data = {
        "total": User.objects.count(),
        "rows": rows
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


from django.db import connection


# 获取当日新增数据
def newdata(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "select count(id) from {0} where DATE_FORMAT(NOW(), '%Y-%m-%d') = FROM_UNIXTIME(adddate, '%Y-%m-%d')".format(
                DjangoBootstrapTableWebConfig.name + USER_TABLE_SUFFIX))
        count = cursor.fetchone()[0]
    data = {
        "newcount": count,
        "username": "admin"
    }
    return JsonResponse(data)


# 分组统计
def datacount(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "select count(id) num, FROM_UNIXTIME(adddate, '%Y-%m-%d') adddate from {0} group by FROM_UNIXTIME(adddate, '%Y-%m-%d')".format(
                DjangoBootstrapTableWebConfig.name + USER_TABLE_SUFFIX))
        sum = cursor.fetchall()
    d = []
    c = []
    for s in sum:
        d.append(s[0])
        c.append(s[1])
    data = {
        "d": d,
        "c": c
    }
    return JsonResponse(data)


def test(request):
    data = {
        "name": "hello",
        "sex": "男",
        "request": request
    }
    return render(request, 'test.html', data)


def hello(request):
    print("aaa")
    return HttpResponse("hello world!")


# redirect响应
def redirect(request):
    return HttpResponseRedirect(reverse("django_bootstrap_table:detail", args=(1,)))


# 使用raw查询
def raw_user(request):
    user_id = request.GET.get("id", default=1)
    raw_user = User.objects.raw(
        "select * from {0} where id={1}".format(DjangoBootstrapTableWebConfig.name + USER_TABLE_SUFFIX, user_id))
    return JsonResponse(user2dict(raw_user[0]))

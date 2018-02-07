from django.contrib import admin
from django_bootstrap_table_web.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # fields = ['id', 'name', "age", "sex"]
    # 控制管理页面展示的字段
    list_display = ('id', 'name', "age", "sex")
    # 查询过滤器
    list_filter = ['age']
    # 搜索字段
    search_fields = ['name', "sex", "age"]


# 注册User model
admin.site.register(User, UserAdmin)

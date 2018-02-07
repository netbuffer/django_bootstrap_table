from django.urls import path
from . import views

app_name = "django_bootstrap_table"

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("hello", views.hello),
    path("userlist", views.user_list),
    path("newdata", views.newdata),
    path("datacount", views.datacount),
    path("detail", views.detail, name="detail"),
    path("<int:id>", views.detail, name="detail"),
    path("redirect", views.redirect, name="redirect"),
]

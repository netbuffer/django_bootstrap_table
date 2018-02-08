from django.urls import path

from . import views

app_name = "django_bootstrap_table"

urlpatterns = [
    path("", views.user, name="user_controller"),
    path("test", views.test),
    path("hello", views.hello),
    path("userlist", views.user_list),
    path("newdata", views.newdata),
    path("datacount", views.datacount),
    path("detail", views.detail, name="detail"),
    path("delete", views.delete_user, name="delete"),
    path("<int:id>", views.detail, name="detail"),
    path("redirect", views.redirect, name="redirect"),
    path("raw", views.raw_user, name="raw"),
]

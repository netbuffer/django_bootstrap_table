from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("hello", views.hello),
    path("userlist", views.user_list),
    path("newdata", views.newdata),
    path("datacount", views.datacount),
]

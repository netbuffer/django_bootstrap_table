from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("index controller")
    return render(request, "manage.html")

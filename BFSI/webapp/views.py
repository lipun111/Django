from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request):
    return HttpResponse("<h1 style='color:red;font-size:60px'>Welcome to Django</h1>")
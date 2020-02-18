from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request):
    return HttpResponse("<h1 style='color:green;font-size:50px;background-color:yellow;text-align:center'>Welcome to python Django</h1>")


def index_view(request, id):
    return HttpResponse(f"<h1 style='color:green;font-size:50px;background-color:yellow;text-align:center'>Wellcome to index page of-{id} </h1>")


def new_view(request, id):
    return HttpResponse(f"<h1 style='color:green;font-size:50px;background-color:yellow;text-align:center'>Wellcome to page of-{id} </h1>")

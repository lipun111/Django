from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    return HttpResponse("<h1>Home page</h1>")


def index_page(request, year):
    return HttpResponse(f"<h1>Index page of Year{year}")
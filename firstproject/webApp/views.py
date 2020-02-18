from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def hello_world_view(request):
    return HttpResponse("<h1>Hello This is the Django Application")

def date_time_view(request):
    date=datetime.datetime.now()
    s='<h1>The current date and time at server is :' + str(date)+ '</h1>'
    return HttpResponse(s)
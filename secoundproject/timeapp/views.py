from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def time_info_view(request):
    time=datetime.datetime.now()
    s='Hello date and time is :' + str(time)
    return HttpResponse(s)
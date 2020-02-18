from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def greetings_view(request):
    return HttpResponse('Hello Friend Good Morning...Have a nice day')
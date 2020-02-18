from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def home(request):
    return HttpResponse("<a href='/hi'> Hello</a>")


def MyView(request):
    return HttpResponseRedirect(reverse('bye'))


def ByeView(request):
    return HttpResponse("Good Bye")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mypage(request,val1,val2):
    msg = val1+" "+val2+" "+"Django"
    return HttpResponse(msg)

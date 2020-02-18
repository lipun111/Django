from django.shortcuts import render

# Create your views here.


def mytemp(request):
    return render(request, 'webapp/results.html')
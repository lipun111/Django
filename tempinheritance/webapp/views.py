from django.shortcuts import render

# Create your views here.


def home_views(request):
    return render(request, 'myapp/home.html')


def sports_views(request):
    return render(request, 'myapp/sports.html')


def movies_views(request):
    return render(request, 'myapp/movies.html')


def business_views(request):
    return render(request, 'myapp/business.html')

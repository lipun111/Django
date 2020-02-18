from django.shortcuts import render

# Create your views here


def home_view(request):
    return render(request, 'myapp/datingapp.html')


def gallery_view(request):
    return render(request, 'myapp/gallery.html')

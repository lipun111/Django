from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'webapp/welcome.html')


def thankspage(request):
    return render(request, 'webapp/thanks.html')
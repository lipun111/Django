from django.shortcuts import render
import datetime
# Create your views here.


def home(request):
    date = datetime.datetime.now()
    name = "LIPUN"
    mydict = {'date': date, 'name': name}

    return render(request, 'webapp/results.html', mydict)
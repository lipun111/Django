from django.shortcuts import render
import datetime

# Create your views here.


def date_time(request):
    dt_now = datetime.datetime.now()
    name = "PYTHON DJANGO"
    my_dict = {'dt_now': dt_now, 'name': name}
    return render(request, 'webapp/welcome.html',my_dict)
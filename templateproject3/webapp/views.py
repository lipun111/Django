from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = "Hello User!!! Very Good"
    if h<12:
        msg = msg+" Morning!!!!"
    elif h<16:
        msg = msg+" Afternoon!!!!"
    elif h<21:
        msg = msg+" Evening!!!!"
    else:
        msg = msg+" Night!!!!"
    my_dict = {"msg":msg, "date":date}
    return render(request,'webapp/results.html',my_dict)

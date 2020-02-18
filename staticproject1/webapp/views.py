from django.shortcuts import render
from datetime import datetime

# Create your views here.


def staticpage(request, val1, val2, val3):
    date= datetime.now()
    name = "PYTHON DJANGO"
    th = int(date.strftime('%H'))
    if th <12:
        wish = f"Good Morning {val3}"+ val1
    elif th < 16:
        wish = "Good Afternoon"+ val1
    else:
        wish = "Good Night"

    mydict = {'date': date, 'name': name, 'wish': wish,}
    return render(request, 'webapp/welcome.html', mydict)
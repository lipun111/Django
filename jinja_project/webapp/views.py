from django.shortcuts import render
import datetime
# Create your views here.


def time_info(request):
    date = datetime.datetime.now()
    name = "Naresh IT"
    th = int(date.strftime("%H"))
    if th<=12:
        wish = "Good Morning Dude"
    elif th <= 16:
        wish = "Good After-Noon Dude"
    elif th <= 21:
        wish = "Good Eveving"
    else:
        wish = "Good Night"

    my_dict={'date': date, 'name': name, 'wish': wish}
    return  render(request, 'webapp/welcome.html', my_dict)
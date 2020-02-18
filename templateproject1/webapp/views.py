from django.shortcuts import render
import datetime
# Create your views here.


def template_view(request):
    dt = datetime.datetime.now()
    name = 'lipun'
    rollno = 101
    mark = 100
    my_dict = {'date': dt, 'name': name, 'rollno': rollno, 'mark': mark}
    return render(request, 'webapp/results.html', my_dict)

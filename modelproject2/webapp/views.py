from django.shortcuts import render
from webapp.models import Emp
# Create your views here.


def views_page(request):
    data = Emp.objects.all()
    my_dict = {'elist': data}

    return render(request, 'myapp/welcome.html', my_dict)
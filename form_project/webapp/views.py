from django.shortcuts import render
from webapp import forms
# Create your views here.


def form_view(request):
    form = forms.EmpForm()
    my_dict = {'form': form}
    return render(request, 'myapp/welcome.html', my_dict)
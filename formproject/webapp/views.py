from django.shortcuts import render
from webapp import forms
# Create your views here.


def emp_view(request):
    form = forms.Empform()
    return render(request, 'myapp/welcome.html', {'form': form})
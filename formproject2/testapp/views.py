from django.shortcuts import render
from testapp import forms
# Create your views here.
def studentregistrer_view(request):
    form = forms.StudentRegistration()
    return render(request, 'myapp/resister.html', {'form':form})

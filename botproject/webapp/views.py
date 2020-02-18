from django.shortcuts import render
from webapp import forms
from django.http import HttpResponseRedirect
# Create your views here.


def emp_view(request):
    form = forms.Empform()
    if request.method == 'POST':
        form = forms.Empform(request.POST)
        if form.is_valid():
            print("Validation Successful:..")
            print("Name:", form.cleaned_data['name'])
            print("Salary:", form.cleaned_data['salary'])
            return HttpResponseRedirect('thank/')

    else:
        form = forms.Empform()
    return render(request, 'myapp/welcome.html', {'form': form})


def thank_view(request):
    return render(request, 'myapp/thank.html')
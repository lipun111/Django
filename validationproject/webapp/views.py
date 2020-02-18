from django.shortcuts import render
from webapp import forms
from django.http import HttpResponseRedirect
# Create your views here.


def emp_view(request):
    form = forms.EmpForm()
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            print("validations are success...")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])
            return HttpResponseRedirect('/thank')
        else:
            form = forms.EmpForm()
    return render(request, 'myapp/welcome.html', {'form': form})


def thank(request):
    return render(request, 'myapp/thankyou.html')
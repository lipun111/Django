from django.shortcuts import render
from webapp import forms
# Create your views here.


def thank_view(request):
    return render(request, 'myapp/thank.html')


def emp_view(request):
    form = forms.Empform()
    if request.method == 'POST':
        form = forms.Empform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Register Successfully Done")
            return thank_view(request)
    return render(request, 'myapp/welcome.html', {'form': form})
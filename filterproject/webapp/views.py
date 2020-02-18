from django.shortcuts import render
from webapp import forms
from webapp.models import Filter
# Create your views here.


def thank_view(request):
    return render(request, 'myapp/thank.html')


def filter_view(request):
    form = forms.Filterform()
    if request.method == 'POST':
        form = forms.Filterform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Print Successfully..")
            return thank_view(request)
    return render(request, 'myapp/welcome.html', {'form':form})


def upper_view(request):
    data_list = Filter.objects.all()
    return render(request, 'myapp/upper.html', {'data_list': data_list})


def lower_view(request):
    data_list = Filter.objects.all()
    return render(request, 'myapp/lower.html', {'data_list': data_list})

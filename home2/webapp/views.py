from django.shortcuts import render
from webapp import forms
from webapp.models import Gpl
# Create your views here.


def thank_view(request):
    return render(request, 'myapp/thank.html')


def home_view(request):
    form = forms.Gplform()
    if request.method == 'POST':
        form = forms.Gplform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thank_view(request)
    return render(request, 'myapp/welcome.html', {'form': form})


def show_view(request):
    data = Gpl.objects.all()
    return render(request, 'myapp/show.html', {'data': data})
from django.shortcuts import render
from webapp.forms import NameForm, AgeForm, GFForm
# Create your views here.


def name_view(request):
    form = NameForm()
    return render(request, 'myapp/name.html', {'form': form})


def age_view(request):
    name = request.GET['name']
    request.session['name'] = name
    form = AgeForm()
    return render(request, 'myapp/age.html', {'form': form})


def gf_view(request):
    age = request.GET['age']
    request.session['age'] = age
    form = GFForm()
    return render(request, 'myapp/gf.html', {'form': form})


def results_view(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'myapp/results.html')

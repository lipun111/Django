from django.shortcuts import render
from movieapp import forms
from movieapp.models import Movie
# Create your views here.


def index_view(request):
    return render(request, 'myapp/index.html')


def addmovie_view(request):
    form = forms.Movieform()
    if request.method == 'POST':
        form = forms.Movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Adding Successfully")
            return index_view(request)
    return render(request, 'myapp/addmovie.html', {'form': form})


def movielist_view(request):
    movielist = Movie.objects.all()
    return render(request, 'myapp/movielist.html', {'movie': movielist})
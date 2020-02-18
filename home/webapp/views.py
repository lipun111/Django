from django.shortcuts import render
from webapp import forms
from webapp.models import Player
# Create your views here.


def thank_view(request):
    return render(request, 'myapp/thank.html')


def player_view(request):
    form = forms.PlayerForm()
    if request.method == 'POST':
        form = forms.PlayerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thank_view(request)
    return render(request, 'myapp/welcome.html', {'form': form})


def show_view(request):
    all_player = Player.objects.all()
    return render(request, 'myapp/show.html',{'all_player': all_player})
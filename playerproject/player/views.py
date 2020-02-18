from django.shortcuts import render
from player.models import Player
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.
class player_list_view(ListView):
    model = Player

class player_detail_view(DetailView):
    model = Player

class player_create_view(CreateView):
    model = Player
    fields = '__all__'

class player_update_view(UpdateView):
    model = Player
    # fields = ['category', 'grade', 'price', 'phoneno']
    fields = '__all__'

class player_delete_view(DeleteView):
    model = Player
    success_url = reverse_lazy('Home')

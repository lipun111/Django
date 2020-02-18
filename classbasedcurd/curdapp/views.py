from django.shortcuts import render
from curdapp.models import Company
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Company_list_view(ListView):
    model = Company

class Company_Detail_view(DetailView):
    model = Company

class Compay_create_view(CreateView):
    model = Company
    fields ='__all__'

class Company_update_view(UpdateView):
    model = Company
    fields = '__all__'

class Company_delete_view(DeleteView):
    model = Company
    success_url = reverse_lazy('home')

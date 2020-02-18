from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from webapp.models import Emplyoee
from django.urls import reverse_lazy
# Create your views here.

class Home_List_View(ListView):
    model = Emplyoee

class Emp_Craete_View(CreateView):
    model = Emplyoee
    fields = '__all__'

class Emp_Detail_View(DetailView):
    model = Emplyoee

class Emp_Update_view(UpdateView):
    model = Emplyoee
    fields = '__all__'

class Emp_Delete_View(DeleteView):
    model = Emplyoee
    success_url = reverse_lazy('home')

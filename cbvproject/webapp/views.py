from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.


class Homeview(View):
    def get(self, request):

        return HttpResponse('<h2> Wlecome to class based view </h2>')


class HomeTemplateView(TemplateView):
    template_name = 'myapp/results.html'


class HomeContexView(TemplateView):
    template_name = 'myapp/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Lipun'
        context['subject'] = 'ptyhon'
        context['mark'] = 100
        return context

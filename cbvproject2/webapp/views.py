from django.shortcuts import render
from django.views.generic import ListView, DetailView
from webapp.models import Book
# Create your views here.

class BookListView(ListView):
    model = Book

    #defult context object: book_list
    #defult template file: book_list.html

class BookDetailView(DetailView):
    model = Book

from django.shortcuts import render
from webapp.forms import AddForm


def add_item_view(request):
    form = AddForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
    return render(request, 'myapp/additem.html', {'form': form})


def display_item_view(request):

    return render(request, 'myapp/showitems.html')

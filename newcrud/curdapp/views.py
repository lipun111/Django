from django.shortcuts import render, redirect
from curdapp.models import Company
from curdapp import forms
# Create your views here.

def show_view(request):
    data = Company.objects.all()
    return render(request, 'curdapp/show.html', {'data':data})

def create_view(request):
    form = forms.CompanyForm()
    if request.method == 'POST':
        form = forms.CompanyForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    return render(request, 'curdapp/create.html', {'form':form})

def update_view(request, id):
    data = Company.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CompanyForm(request.POST, instance=data)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        # else:
        #     form = forms.CompanyForm()
    return render(request, 'curdapp/update.html', {'data':data})

def delete_view(request,id):
    data = Company.objects.get(id=id)
    data.delete()
    return redirect('home')

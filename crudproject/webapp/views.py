from django.shortcuts import render, redirect
from webapp.models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from webapp.forms import SignupForm, InsertForm
# Create your views here.

def home_view(request):
    return render(request, 'myapp/home.html')

@login_required
def index_view(request):
    employee = Employee.objects.all()
    return render(request,'myapp/index.html', {'employee':employee})

def logout_view(request):
    return render(request, 'myapp/logout.html')

def signup_view(request):
    form = SignupForm()
    if request.method =='POST':
        form = SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('/accounts/login')

    return render(request,'myapp/signup.html', {'form':form})

def create_view(request):
    form = InsertForm()
    if request.method == 'POST':
        form = InsertForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/info')
    return render(request, 'myapp/insert.html', {'form':form})

def delete_view(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/info')


def update_view(request, id):
    employee = Employee.objects.get(id=id)
    if request.method =='POST':
        form = InsertForm(request.POST, instance=employee)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/info')
    return render(request, 'myapp/update.html', {'emp':employee})

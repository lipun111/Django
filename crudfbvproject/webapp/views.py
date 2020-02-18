from django.shortcuts import render, redirect
from webapp.models import Employee
from webapp.forms import EmployeeForm
# Create your views here.
def retrive_view(request):
    employee = Employee.objects.all()
    return render(request,'myapp/index.html', {'employee':employee})

def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request, 'myapp/create.html', {'form': form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method =='POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request, 'myapp/update.html', {'emp':employee})

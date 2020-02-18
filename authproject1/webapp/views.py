from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webapp.forms import SignupForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'myapp/home.html')

@login_required
def business_view(request):
    return render(request,'myapp/business.html')

@login_required
def soprts_view(request):
    return render(request,'myapp/sport.html')

def logout_view(request):
    return render(request,'myapp/logout.html')

def signup_view(request):
    form = SignupForm()
    if request.method =='POST':
        form = SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'myapp/signup.html', {'form':form})

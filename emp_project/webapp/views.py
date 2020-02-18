from django.shortcuts import render
from webapp import forms
# Create your views here.


def thank_view(request):
    return render(request, 'myapp/thank.html')


def signup_view(request):
    form = forms.Signupform()
    if request.method == 'POST':
        form = forms.Signupform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Signup Successfully Done...")
            return thank_view(request)
    return render(request, 'myapp/welcome.html', {'form': form})
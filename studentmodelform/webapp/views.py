from django.shortcuts import render
from webapp import forms
# Create your views here.


def thank_view(request):
    return render(request, 'myapp/thank.html')


def student_view(request):
    form = forms.Studentform()
    if request.method == 'POST':
        form = forms.Studentform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Successfully register....")
            return thank_view(request)
    return render(request, 'myapp/welcome.html', {'form': form})

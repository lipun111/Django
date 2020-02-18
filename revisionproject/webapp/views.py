from django.shortcuts import render, redirect
from webapp.models import Revision
from webapp.forms import RevisionForm
# Create your views here.r


def show_view(request):
    data = Revision.objects.all()
    return render(request, 'webapp/show.html', {'data':data})

def home_view(request):
    form = RevisionForm()
    if request.method == 'POST':
        form = RevisionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    return render(request, 'webapp/results.html', {'form':form})

from django.shortcuts import render
from testapp import forms

# Create your views here.
def thank_views(request):
    return render(request,'myapp/thank.html')


def feedback_view(request):
    if request.method == 'GET':
        form = forms.FeedbackForm()
        return render(request, 'myapp/feedback.html',{'form':form})
    if request.method =='POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            print("Form validation successfull and printing data:")
            print("Student Name:", form.cleaned_data['name'])
            print("Student RollNo:", form.cleaned_data['rollno'])
            print("Student Mail:", form.cleaned_data['email'])
            print("Student Feedback:", form.cleaned_data['feedback'])
            return thank_views(request)
    return render(request, 'myapp/feedback.html',{'form':form})

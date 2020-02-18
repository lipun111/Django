from django.shortcuts import render

# Create your views here.

def name_view(request):
    return render(request, 'myapp/name.html')

def age_view(request):
    name = request.GET['name'] #reading data from hrml page.
    response = render(request, 'myapp/age.html')
    response.set_cookie('name',name) #saved data to cookies
    return response

def gf_view(request):
    age = request.GET['age'] #reading data from hrml page.
    response = render(request, 'myapp/gf.html')
    response.set_cookie('age', age) #saved data to cookies
    return response


def result_view(request):
    gfname = request.GET['gfname'] #reading data from hrml page.
    name = request.COOKIES.get('name') #fatching data from cookies.
    age = request.COOKIES.get('age') #fatching data from cookies.
    response = render(request, 'myapp/results.html', {'name': name,'age': age, 'gfname': gfname})
    return response

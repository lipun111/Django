from django.shortcuts import render

# Create your views here.


def page_count_view(request):
    count = request.session.get('count', 0)
    newcount = count+1
    request.session['count'] = newcount
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request, 'myapp/pagecount.html',{'cont':newcount})
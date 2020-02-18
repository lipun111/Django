from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    return render(request, 'myapp/homenews.html')


def movie_page_view(request):
    news1= 'In Hindi Chichore movie is very good'
    news2= 'IN Odia Akhire Akire movie is very good'
    news3= 'fjkdhfjhh;lkjflkjvsdkjl'
    news4= 'dkfkriojgiskalklnvfdlknvjnnrwnkjrenjnf'
    news5= 'kkfjeriwjijrnvjfnvjnfdjsnsjkfnfkjnjkank'
    news6= 'asdfghjkl'
    news7= 'fnvklnfknviroionwkfklnvkln'
    mydict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5,'news6':news6,'news7':news7}
    return render(request, 'myapp/mnews.html', mydict)


def sport_page_view(request):
    return render(request, 'myapp/snews.html')


def business_page_view(request):
    return render(request, 'myapp/bnews.html')

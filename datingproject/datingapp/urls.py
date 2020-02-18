
from django.urls import path
from datingapp import views
urlpatterns = [

    path('', views.home_view, name='home'),
    path('gallery/', views.gallery_view, name='gallery'),
]
from django.contrib import admin
from django.urls import path
from curdapp import views
urlpatterns = [
    path('', views.show_view, name='home'),
    path('add/', views.create_view, name='add'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
]

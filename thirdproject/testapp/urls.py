
from django.urls import path
from testapp import views
urlpatterns = [
    path('first/', views.first_view),
    path('secound/', views.secound_view),
    path('third/', views.third_view),
    path('fourth/', views.fourth_view),
    path('fifth/', views.fifth_view),

]

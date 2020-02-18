
from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.Home_List_View.as_view(), name='home' ),
    path('create/', views.Emp_Craete_View.as_view(), name='create' ),
    path('detail/<int:pk>', views.Emp_Detail_View.as_view(), name='detail' ),
    path('update/<int:pk>', views.Emp_Update_view.as_view(), name='update' ),
    path('delete/<int:pk>', views.Emp_Delete_View.as_view(), name='delete' ),
]

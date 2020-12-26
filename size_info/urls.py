from django.urls import path
from . import views

urlpatterns = [
    path('girl_size_info/', views.girl_size_info, name='girl_size_info'),
    path('women_size_info/', views.women_size_info, name='women_size_info'),
    path('boy_size_info/', views.boy_size_info, name='boy_size_info'),
    path('men_size_info/', views.men_size_info, name='men_size_info'),
]

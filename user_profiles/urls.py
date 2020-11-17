from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profiles, name='user_profiles'),
    path('order_history/<order_number>', views.order_history, name='order_history'),

]

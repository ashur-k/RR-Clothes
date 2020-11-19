from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path('add/', views.add_product, name='add_product'),
    path('add_variant/<int:product_id>/', views.add_variant, name='add_variant'),
    path('edit_product_variant/<int:product_id>/', views.edit_product_variant, name='edit_product_variant'),
    path('edit_variant/<int:variant_id>/', views.edit_variant, name='edit_variant'),
]

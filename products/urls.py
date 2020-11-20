from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path('add/', views.add_product, name='add_product'),
    path('add_variant/<int:product_id>/', views.add_variant, name='add_variant'),
    path('product_management/<int:product_id>/', views.product_management, name='product_management'),
    path('edit_product_with_variant/<int:product_id>/', views.edit_product_with_variant, name='edit_product_with_variant'),
    path('edit_product_without_variant/<int:product_id>/<int:variant_id>/', views.edit_product_without_variant, name='edit_product_without_variant'),
    path('edit_variant/<int:product_id>/<int:variant_id>/', views.edit_variant, name='edit_variant'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_variant/<int:variant_id>/', views.delete_variant, name='delete_variant'),
]

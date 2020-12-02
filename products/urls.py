from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path('add/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_variant/<int:product_id>/', views.add_variant, name='add_variant'),
    path('product_management/<int:product_id>/', views.product_management, name='product_management'),
    path('edit_product_with_variant/<int:product_id>/', views.edit_product_with_variant, name='edit_product_with_variant'),
    path('edit_product_without_variant/<int:product_id>/<int:variant_id>/', views.edit_product_without_variant, name='edit_product_without_variant'),
    path('edit_variant/<int:product_id>/<int:variant_id>/', views.edit_variant, name='edit_variant'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_variant/<int:variant_id>/', views.delete_variant, name='delete_variant'),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('add_comment/<int:product_id>/', views.add_comment, name='add_comment'),
    path('add_color/', views.add_color, name='add_color'),
    path('add_size/', views.add_size, name='add_size'),
    path('delete_color/<int:product_id>/<int:variant_id>/<int:color_id>/', views.delete_color, name='delete_color'),
    path('delete_size/<int:product_id>/<int:variant_id>/<int:size_id>/', views.delete_size, name='delete_size'),
    path('color_management/', views.color_management, name='color_management'),
    path('ajax_add_color',  views.ajax_add_color, name='ajax_add_color'),
    path('ajax_edit_color',  views.ajax_edit_color, name='ajax_edit_color'),
    path('ajax_delete_color', views.ajax_delete_color, name='ajax_delete_color'),
    path('size_management/', views.size_management, name='size_management'),
    path('ajax_add_size',  views.ajax_add_size, name='ajax_add_size'),
    path('ajax_edit_size',  views.ajax_edit_size, name='ajax_edit_size'),
]

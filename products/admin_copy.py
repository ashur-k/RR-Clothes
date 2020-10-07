from django.contrib import admin
from .models import Product, Category, ProductUnit, ProductSize, ProductDetail, ProductColour


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
    
        'name',
        'category',
        'price',
        'rating',
        'image',
    )




class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_name',
        'name',
    )


class ProductUnitAdmin(admin.ModelAdmin):
    list_display = (
        'product_unit_name',
        'product_unit_short_name'

    )


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = (
        'size',
        'friendly_size_name',
    )


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'size',
        'product_unit',
        'product_colour',
        'initial_quantity',
        'initial_date',
        

    )


class ProductColourAdmin(admin.ModelAdmin):
    list_display = (
        'colour',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductUnit, ProductUnitAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(ProductColour, ProductColourAdmin)

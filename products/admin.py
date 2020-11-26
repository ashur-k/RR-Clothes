import admin_thumbnails
from django.contrib import admin
from .models import Category, Product, Images, Color, Size, Variants, Comment


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'image',
        'id'
    )


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 1


class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag', 'product_id', 'id')
    extra = 1
    show_change_link = True


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'title', 'image_thumbnail')


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'discount_30_percent', 'has_variant', 'variant', 'category', 'status', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline, ProductVariantsInline]


class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'color_tag']


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


class VariantsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'product',
        'color',
        'size',
        'price',
        'quantity',
        'image_tag'
        ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'subject', 'rate']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Variants, VariantsAdmin)
admin.site.register(Comment, CommentAdmin)

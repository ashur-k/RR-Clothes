from django.contrib import admin
from .models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)

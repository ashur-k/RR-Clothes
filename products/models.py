from django.db import models
import datetime


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductUnit(models.Model):
    product_unit_name = models.CharField(max_length=100)
    product_unit_short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.product_unit_name


class ProductSize(models.Model):
    size = models.CharField(max_length=100)
    friendly_size_name = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=254)
    product_unit_id = models.ForeignKey('ProductUnit', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductColour(models.Model):
    colour = models.CharField(max_length=10)

    def __str__(self):
        return self.colour


class ProductDetail(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    size_id = models.ForeignKey('ProductSize', null=True, blank=True, on_delete=models.SET_NULL)
    initial_quantity = models.BigIntegerField(default=9999)
    product_colour_id = models.ForeignKey('ProductColour', null=True, blank=True, on_delete=models.SET_NULL)
    initial_date = datetime.datetime.now()

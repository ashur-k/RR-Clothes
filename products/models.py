from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from decimal import Decimal


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    image = models.ImageField(blank=True, upload_to='media/')
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def image_tag(self):
        if self.image.url:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return mark_safe('<img src="" height="50"/> alt="no img"')


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),
    )

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=False, upload_to='media/')
    price = models.FloatField()
    rate = models.IntegerField(default=1)
    quantity = models.IntegerField()
    has_variant = models.BooleanField(default=False, null=True, blank=True)
    new_edition = models.BooleanField(default=False, null=True, blank=True)
    discount_30_percent = models.BooleanField(default=False, null=True, blank=True)
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def product_reviews(self):
        reviews = Comment.objects.filter(product=self)
        return reviews

    def averagereviews(self):
        reviews = Comment.objects.filter(product=self).aggregate(average=Avg('rate'))
        avg = 0
        if reviews["average"] is not None:
            avg = float(reviews["average"])
        return avg

    def counterview(self):
        reviews = Comment.objects.filter(product=self).aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

    def percent_30_discount(self):
        if self.discount_30_percent == 1:
            discount_price = self.price * 30 / 100
            return discount_price


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=False, upload_to='media/')

    class Meta:
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.title


class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null='True')

    class Meta:
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.name


class Variants(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True, default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS, default=True)

    class Meta:
        verbose_name_plural = 'Variants'

    def get_size(self):
        return "a"

    def __str__(self):
        return self.title

    def percent_30_discount(self):
        if self.product.discount_30_percent == 1:
            discount_price = self.price * 30 / 100
            return discount_price

    def image(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            varimage = img.image.url
        else:
            varimage = ""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    rate = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

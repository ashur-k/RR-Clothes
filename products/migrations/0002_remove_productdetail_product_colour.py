# Generated by Django 3.1.1 on 2020-10-07 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='product_colour',
        ),
    ]
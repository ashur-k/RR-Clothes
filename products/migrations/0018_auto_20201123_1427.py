# Generated by Django 3.1.1 on 2020-11-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-11-07 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product',
        ),
    ]
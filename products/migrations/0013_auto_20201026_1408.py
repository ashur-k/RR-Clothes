# Generated by Django 3.1.1 on 2020-10-26 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20201024_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': 'Colors'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name_plural': 'Sizes'},
        ),
        migrations.AlterModelOptions(
            name='variants',
            options={'verbose_name_plural': 'Variants'},
        ),
    ]
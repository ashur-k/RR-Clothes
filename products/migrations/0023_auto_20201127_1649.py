# Generated by Django 3.1.1 on 2020-11-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20201127_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variants',
            name='images',
        ),
        migrations.AlterField(
            model_name='variants',
            name='image_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

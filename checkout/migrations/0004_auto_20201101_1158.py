# Generated by Django 3.1.1 on 2020-11-01 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20201101_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_adderss1',
            new_name='street_address1',
        ),
    ]

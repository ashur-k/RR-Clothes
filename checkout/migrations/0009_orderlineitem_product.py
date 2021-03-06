# Generated by Django 3.1.1 on 2020-11-07 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_has_variant'),
        ('checkout', '0008_remove_orderlineitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-05 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20201005_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductColour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='productdetail',
            name='product_colour_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productcolour'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-11-03 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
        ('checkout', '0006_auto_20201103_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='user_profiles.userprofile'),
        ),
    ]
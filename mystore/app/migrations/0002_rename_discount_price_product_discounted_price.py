# Generated by Django 4.0.5 on 2022-12-08 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_price',
            new_name='discounted_price',
        ),
    ]

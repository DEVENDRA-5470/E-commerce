# Generated by Django 4.0.5 on 2022-12-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer_mob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='localtiy',
            new_name='locality',
        ),
    ]
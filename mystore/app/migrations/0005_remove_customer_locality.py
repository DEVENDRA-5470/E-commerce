# Generated by Django 4.0.5 on 2022-12-13 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_localtiy_customer_locality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='locality',
        ),
    ]

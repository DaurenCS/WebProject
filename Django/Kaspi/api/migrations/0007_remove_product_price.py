# Generated by Django 3.2 on 2023-05-03 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_store_storeitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]

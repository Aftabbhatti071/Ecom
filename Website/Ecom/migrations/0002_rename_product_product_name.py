# Generated by Django 5.0.6 on 2024-06-22 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='name',
        ),
    ]

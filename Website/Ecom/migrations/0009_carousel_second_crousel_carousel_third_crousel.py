# Generated by Django 5.0.6 on 2024-06-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0008_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='second_crousel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='carousel',
            name='third_crousel',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]

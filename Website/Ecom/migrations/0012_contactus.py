# Generated by Django 5.0.6 on 2024-06-26 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0011_promotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]

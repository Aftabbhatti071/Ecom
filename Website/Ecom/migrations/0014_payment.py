# Generated by Django 5.0.6 on 2024-06-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecom', '0013_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('stripe_charge_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

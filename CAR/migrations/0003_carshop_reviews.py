# Generated by Django 4.1.7 on 2023-03-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAR', '0002_carshop_manufacturing_country_carshop_model_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carshop',
            name='reviews',
            field=models.TextField(null=True, verbose_name='Отзывы'),
        ),
    ]
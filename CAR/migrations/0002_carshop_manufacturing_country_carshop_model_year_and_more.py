# Generated by Django 4.1.7 on 2023-03-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAR', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carshop',
            name='manufacturing_country',
            field=models.TextField(null=True, verbose_name='Страна изготовитель'),
        ),
        migrations.AddField(
            model_name='carshop',
            name='model_year',
            field=models.TextField(null=True, verbose_name='Модельный год'),
        ),
        migrations.AddField(
            model_name='carshop',
            name='specifications',
            field=models.TextField(null=True, verbose_name='Характеристики'),
        ),
    ]
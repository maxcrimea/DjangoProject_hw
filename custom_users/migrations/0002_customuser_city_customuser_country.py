# Generated by Django 4.1.7 on 2023-04-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='Город проживания'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(max_length=100, null=True, verbose_name='Ваша страна'),
        ),
    ]

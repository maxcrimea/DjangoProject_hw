# Generated by Django 4.1.7 on 2023-03-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название модели')),
                ('description', models.TextField(verbose_name='Описание автомобиля')),
                ('image', models.ImageField(upload_to='')),
                ('car_type', models.CharField(choices=[('Для молодых людей', 'Для молодых людей'), ('Для работы', 'Для работы'), ('Для большой семьи', 'Для большой семье'), ('Для путешествий', 'Для путешествий'), ('Для женщин', 'Для женщин'), ('Для успешных', 'Для успешных')], max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('cost', models.PositiveIntegerField()),
                ('video', models.URLField()),
            ],
        ),
    ]

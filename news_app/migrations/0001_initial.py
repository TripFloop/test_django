# Generated by Django 3.2 on 2021-04-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название новости')),
                ('content', models.TextField(max_length=1000, verbose_name='Контент')),
                ('publication_data', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-04-11 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_app', '0003_rename_publication_data_news_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

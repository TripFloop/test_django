from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название новости")
    content = models.TextField(max_length=1000, verbose_name="Контент")
    publication_date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(blank=True)

from django.db import models


class News(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название новости")
    content = models.TextField(max_length=1000, verbose_name="Контент")
    publication_date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

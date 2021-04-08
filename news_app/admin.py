from django.contrib import admin
from .models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # Model View in Django admin
    list_display = ("id", "name", "content", "publication_date")
    list_display_links = ("name",)
    date_hierarchy = "publication_date"
    search_fields = ("name",)
    readonly_fields = ("id", "publication_date")
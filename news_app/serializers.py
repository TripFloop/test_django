from rest_framework import serializers

from .models import News


class NewsListSerializer(serializers.ModelSerializer):
    """ List of News """

    class Meta:
        model = News
        fields = ("name", "content", "publication_date")


class NewsDetailSerializer(serializers.ModelSerializer):
    """ Single news """

    class Meta:
        model = News
        fields = ("id", "name", "content", "publication_date")

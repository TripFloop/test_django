from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsListSerializer, NewsDetailSerializer


def get_news(news_id):
    try:
        return News.objects.get(id=news_id)
    except News.DoesNotExist:
        return Response(status=404)


class NewsListView(APIView):
    """Show all News, existing in DB"""

    def get(self, request):
        news = News.objects.all()
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)


class NewsDetailView(APIView):
    """Show single News with id = pk"""

    def get(self, request, pk):
        news = get_news(pk)
        if isinstance(news, Response):  # Bad practice
            return Response(status=404)
        serializer = NewsDetailSerializer(news)
        return Response(serializer.data)


class NewsCreateView(APIView):
    """Create new News"""

    def post(self, request):
        news = NewsDetailSerializer(data=request.data)
        if news.is_valid():
            news.save()
        else:
            return Response(status=422)  # or Response(status=400)?
        return Response(status=201)


class NewsDeleteView(APIView):
    """Delete News with id = pk"""

    def delete(self, request, pk):
        news = get_news(pk)
        if isinstance(news, Response):  # Bad practice
            return Response(status=404)
        news.delete()
        return Response(status=204)


class NewsUpdateView(APIView):
    """Update News with id = pk"""

    def put(self, request, pk):
        news = get_news(pk)
        if isinstance(news, Response):  # Bad practice
            return Response(status=404)
        serializer = NewsDetailSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

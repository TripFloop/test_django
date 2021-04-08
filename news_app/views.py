from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .serializers import NewsListSerializer, NewsDetailSerializer


def get_news(id):
    try:
        return News.objects.get(id=id)
    except News.DoesNotExist:
        return Response(status=404)


class NewsListView(APIView):

    def get(self, request):
        news = News.objects.all()
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)


class NewsDetailView(APIView):

    def get(self, request, pk):
        news = get_news(id=pk)
        serializer = NewsDetailSerializer(news)
        print(serializer.data)
        return Response(serializer.data)


class NewsCreateView(APIView):

    def post(self, request):
        news = NewsDetailSerializer(data=request.data)
        if news.is_valid():
            news.save()
        return Response(status=201)


class NewsDeleteView(APIView):

    def delete(self, request, pk):
        news = get_news(id=pk)
        news.delete()
        return Response(status=204)


class NewsUpdateView(APIView):

    def put(self, request, pk):
        news = get_news(id=pk)
        serializer = NewsDetailSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

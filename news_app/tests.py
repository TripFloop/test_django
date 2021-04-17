import json

from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from news_app.models import News
from news_app.serializers import NewsListSerializer, NewsDetailSerializer

factory = APIRequestFactory()


# CREATE
class CreateNewsTestCase(APITestCase):

    def test_news_creation(self):
        data = {"name": "testName", "content": "Test content"}
        response = self.client.post("/api/news/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_wrong_news_creation(self):
        data = {"wrong_name": "testName", "content": "Test content"}  # Wrong attribute name
        response = self.client.post("/api/news/create/", data)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)  # Or status.HTTP_400_BAD_REQUEST


# READ - MANY
class ListNewsTestCase(APITestCase):

    def test_news_list(self):
        for iter in range(5):
            News.objects.create(name=f"testName{iter}", content=f"Test content{iter}")
        raw_data = News.objects.all()
        serializer = NewsListSerializer(raw_data, many=True)
        response = self.client.get("/api/news/")
        self.assertEqual(response.data, serializer.data)


# READ - SINGLE
class SingleNewsTestCase(APITestCase):

    def test_single_news(self):
        test_news = News.objects.create(name="testName", content="Test content")
        raw_data = News.objects.get(id=test_news.id)
        serializer = NewsDetailSerializer(raw_data)
        response = self.client.get(f"/api/news/{test_news.id}", follow=True)
        self.assertEqual(response.data, serializer.data)

    def test_null_news(self):
        response = self.client.get("/api/news/12", follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# UPDATE AND DELETE

class UpdateNewsTestCase(APITestCase):

    def test_update_news(self):
        test_news = News.objects.create(name="testName", content="Test content")
        self.client.post(f"/api/news/update/{test_news.id}", {"name": "testNameUpdate", "content": "Test content Update"})
        serializer = NewsDetailSerializer(News.objects.get(id=test_news.id))
        response = self.client.get(f"/api/news/{test_news.id}", follow=True)
        self.assertEqual(response.data, serializer.data)

    def test_null_update_news(self):
        response = self.client.put("/api/news/update/100", {"name": "testname1"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DeleteNewsTestCase(APITestCase):

    def test_delete_news(self):
        test_news = News.objects.create(name="testName", content="Test content")
        response = self.client.delete(f"/api/news/delete/{test_news.id}/")
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response = self.client.get(f"/api/news/{test_news.id}/")
            self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY) # APPEND_SLASH = True
        else:
            self.fail(f"Status code is not 204 after deleting, status code is {response.status_code}")

    def test_delete_null_news(self):
        response = self.client.delete("/news/delete/100")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

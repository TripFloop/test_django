from django.urls import path

from . import views

urlpatterns = [
    path("news/create/", views.NewsCreateView.as_view()),
    path("news/", views.NewsListView.as_view()),
    path("news/<int:pk>/", views.NewsDetailView.as_view()),
    path("news/update/<int:pk>", views.NewsUpdateView.as_view()),
    path("news/delete/<int:pk>", views.NewsDeleteView.as_view())
]

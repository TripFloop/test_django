from django.urls import path

from . import views_DRF, views

urlpatterns = [
    path("news/create/", views_DRF.NewsCreateView.as_view()),
    path("news/", views_DRF.NewsListView.as_view()),
    path("news/<int:pk>/", views_DRF.NewsDetailView.as_view()),
    path("news/update/<int:pk>/", views_DRF.NewsUpdateView.as_view()),
    path("news/delete/<int:pk>/", views_DRF.NewsDeleteView.as_view()),
]

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from news_app.models import News


def welcoming_view(request):
    return render(request, "index.html")


def news_list_view(request):
    news_list = News.objects.all()
    return render(request, "news_list.html", context={"news_list": news_list})


def welcoming_redirect_view(request):
    # Redirected, because i want a home page with "/home" slug
    return HttpResponseRedirect('/home')


def users_list_view(request):
    # Refactor for 1 queryset except 2, give DB a little break
    users = User.objects.all()
    news = News.objects.all()
    return render(request, "users_with_news.html", context={"users": users,
                                                       "news": news})

from django.shortcuts import render
from app.news.models import News

from django.views.generic import ListView, DetailView
# Create your views here.
# def news(request):
#     news = News.objects.latest("id")
#     return render(request, "index.html", locals())

class NewsListView(ListView):
    template_name = 'index.html'
    model = News
    context_object_name = 'news'

class NewsDetail(DetailView):
    template_name = 'detail.html'
    model = News
    context_object_name = 'news'
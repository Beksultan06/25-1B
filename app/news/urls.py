from django.urls import path
from app.news.views import NewsListView, NewsDetail

urlpatterns = [
    path("", NewsListView.as_view(), name='news'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail')
]
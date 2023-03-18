from django.urls import path
from articles.views.template_views import article_list_view, article_detail_view

urlpatterns = [
    path('', article_list_view, name='article_list'),
    path('articles/<slug:slug>/', article_detail_view, name='article_detail'),
]

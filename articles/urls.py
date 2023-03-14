from django.urls import path
from .views import article_list_view, article_detail_view, comment_list_view

urlpatterns = [
    path('', article_list_view, name='article_list'),
    path('articles/<slug:slug>/', article_detail_view, name='article_detail'),
    path('comments/<slug:slug>/', comment_list_view, name='comment'),
]

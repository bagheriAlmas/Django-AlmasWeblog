from django.urls import path, include
from articles.views.template_views import article_list_view, article_detail_view
from .views.api_views import ArticleView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleView)

urlpatterns = [
    path('', article_list_view, name='article_list'),
    path('articles/<slug:slug>/', article_detail_view, name='article_detail'),
    path('api/articles/', include(router.urls))
]

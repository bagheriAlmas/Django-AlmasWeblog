from ..models import Article
from ..serializers import ArticleSerializer
from rest_framework import viewsets, permissions


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.PublishedArticle.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

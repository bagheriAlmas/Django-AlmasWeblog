from rest_framework import serializers

from articles.models import Article, Category
from .models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'content', 'image', 'read_time', 'resource', 'created', 'author',
                  'categories', 'slug']


class ReporterSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(source='Articles', many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'facebook', 'twitter', 'avatar', 'about_me',
                  'articles']

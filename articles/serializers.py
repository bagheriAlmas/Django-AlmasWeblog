from rest_framework import serializers
from .models import Article, Category
from .models import CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'facebook', 'twitter', 'avatar', 'about_me']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ArticleSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'content', 'image', 'read_time', 'resource', 'created', 'author',
                  'categories', 'slug']

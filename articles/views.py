from django.shortcuts import render

from articles.models import Article


def article_list_view(request):
    articles = Article.PublishedArticle.all()
    return render(request, 'articles/article_list.html', {'articles': articles, 'randomPosts': random_articles(6)})


def article_detail_view(request, slug):
    article = Article.PublishedArticle.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article, 'randomPosts': random_articles(3)})


def random_articles(num):
    articles = Article.PublishedArticle.all()
    random = articles.order_by('?')[:num]
    return random

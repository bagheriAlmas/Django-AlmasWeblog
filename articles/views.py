from django.shortcuts import render

from articles.models import Article


def article_list_view(request):
    # articles = Article.objects.all()
    articles = Article.PublishedArticle.all()
    return render(request, 'article_list.html', {'articles': articles})


def article_detail_view(request, slug):
    article = Article.PublishedArticle.get(slug=slug)
    return render(request, 'article_detail.html', {'article': article})

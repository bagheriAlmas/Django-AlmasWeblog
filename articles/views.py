from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from articles.forms import CommentForm
from articles.models import Article, Comment


def article_list_view(request):
    articles = Article.PublishedArticle.all()
    return render(request, 'articles/article_list.html', {'articles': articles, 'randomPosts': random_articles(6)})


def article_detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article).all()

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.article = article
            obj.save()
            return HttpResponseRedirect(request.path_info)
    else:
        context = {'article': article, 'comments': comments, 'form': form, 'randomPosts': random_articles(3)}
        return render(request, 'articles/article_detail.html', context)


def random_articles(num):
    articles = Article.PublishedArticle.all()
    random = articles.order_by('?')[:num]
    return random


def comment_list_view(request, slug):
    comments = Comment.objects.filter(article__slug=slug)
    return render(request, 'test.html', {'comments': comments})

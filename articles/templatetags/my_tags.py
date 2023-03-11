from datetime import datetime

from django import template

from articles.models import Article

register = template.Library()


@register.simple_tag()
def articles_count():
    return Article.PublishedArticle.count()


@register.filter(name='is_new')
def new_article(value):
    created_date = value.strftime("%d %m %y")
    now_date = datetime.now().strftime("%d %m %y")
    created_date_prime = datetime.strptime(created_date, '%d %m %y')
    created_date_now = datetime.strptime(now_date, '%d %m %y')

    return (created_date_now - created_date_prime).days < 7

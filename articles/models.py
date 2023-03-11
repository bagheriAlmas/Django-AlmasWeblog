from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime

from users.models import CustomUser


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Article(models.Model):
    objects = models.Manager()
    PublishedArticle = PublishedManager()
    ARTICLE_STATUS = (
        ('checking', 'Checking'),
        ('rejected', 'Rejected'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Articles')
    status = models.CharField(max_length=15, choices=ARTICLE_STATUS, default='checking')
    image = models.ImageField(upload_to='images/%Y/%m/%d',blank=True,null=True)
    categories = models.ManyToManyField('Category', blank=True)
    read_time = models.PositiveSmallIntegerField()
    resource = models.CharField(max_length=300, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)


    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = slugify(self.title) + "-" + str(now.year) + "-" + str(now.month) + "-" + str(now.day)
            self.save()

    def __str__(self):
        return f"({self.title}) --------> [{self.author}]"

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField( max_length=50)
    is_enable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

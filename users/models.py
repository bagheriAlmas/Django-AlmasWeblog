from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(null=True,blank=True)
    facebook = models.CharField(max_length=200, null=True,blank=True)
    twitter = models.CharField(max_length=200, null=True,blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True,blank=True , default='default_user.jpg')
    about_me = models.TextField(null=True, blank=True)

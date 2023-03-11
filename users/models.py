from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(null=True)
    instagram = models.CharField(max_length=200, null=True)
    twitter = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(upload_to='avatars', null=True,blank=True)
    about_me = models.TextField(null=True, blank=True)

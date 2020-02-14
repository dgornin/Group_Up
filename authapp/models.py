from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='User age')
    about_me = models.TextField(max_length=1000, verbose_name='description', blank=True)
    vk_url = models.URLField(max_length=250, blank=True)
    telegram_url = models.URLField(max_length=250, blank=True)
    instagram_url = models.URLField(max_length=250, blank=True)


class UserSubscribe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    subscribe = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribe')


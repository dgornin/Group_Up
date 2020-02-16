from django.db import models
from django.conf import settings
import uuid

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=30, verbose_name='Group name')
    profile_photo = models.ImageField(upload_to='group_photo', verbose_name='Group_profile_photo', blank=True)
    short_desc = models.CharField(verbose_name='short_description', max_length=60, blank=True)
    description = models.TextField(verbose_name='description', blank=True)
    uuid = models.UUIDField(verbose_name='uuid', blank=True, default=uuid.uuid4())


class Available(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='available')
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
    add_datetime = models.DateTimeField(verbose_name='add_datetime', auto_now_add=True)


class Task(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='task_name', max_length=60)
    description = models.TextField(verbose_name='description')
    is_done = models.BooleanField(verbose_name='is_done', default=False)

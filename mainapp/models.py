from django.db import models


# Create your models here.
class User(models.Model):
    nick_name = models.CharField(max_length=30, verbose_name='Nick name')
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    date_of_birth = models.DateField(verbose_name='Date of birth')
    profile_photo = models.ImageField(upload_to='user_photo', verbose_name='User profile photo')


class Group(models.Model):
    name = models.CharField(max_length=30, verbose_name='Group name')
    profile_photo = models.ImageField(upload_to='group_photo', verbose_name='Group profile photo')

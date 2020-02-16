from django.contrib import admin
from .models import CustomUser, UserSubscribe


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserSubscribe)


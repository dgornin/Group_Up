from django.contrib import admin
from .models import Group, Available, Task


# Register your models here.
admin.site.register(Group)
admin.site.register(Available)
admin.site.register(Task)

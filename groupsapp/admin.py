from django.contrib import admin
from .models import Group, Available, Task, Permission


# Register your models here.
admin.site.register(Group)
admin.site.register(Available)
admin.site.register(Task)
admin.site.register(Permission)

from django.urls import path
import groupsapp.views as controller


app_name = 'groupsapp'

urlpatterns = [
    path('', controller.index, name='index'),
    path('add/<int:id>', controller.add_user, name='add_user'),
    path('remove/<int:id>', controller.remove_user, name='remove_user'),
    path('group/<int:id>/<str:key>', controller.group, name='group'),
]

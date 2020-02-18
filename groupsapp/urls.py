from django.urls import path
import groupsapp.views as controller

from Group_Up.groupsapp import views

app_name = 'groupsapp'

urlpatterns = [
    path('', controller.index, name='index'),
    path('add/<int:id>/<str:key>', controller.add_user, name='add_user'),
    path('remove/<int:id>/<str:key>', controller.remove_user, name='remove_user'),
    path('group/<int:id>/<str:key>', controller.group, name='group'),
    path('new_group/', controller.new_group, name='new_group'),
    path('task/', views.tasks, name='task'),

]

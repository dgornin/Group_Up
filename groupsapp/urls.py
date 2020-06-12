from django.urls import path
import groupsapp.views as controller


app_name = 'groupsapp'

urlpatterns = [
    path('', controller.index, name='index'),
    path('add/<int:id>/<str:key>', controller.add_user, name='add_user'),
    path('remove/<int:id>/<str:key>', controller.remove_user, name='remove_user'),
    path('group/<int:id>/<str:key>', controller.group, name='group'),
    path('new_group/', controller.new_group, name='new_group'),
    path('task/<int:id>/<str:key>', controller.task, name='task'),
    path('all_tasks/<str:key>', controller.all_tasks, name='all_tasks'),
    path('new_task/<int:id>', controller.new_task, name='new_task'),
    path('edit_group/<int:id>/<str:key>', controller.edit_group, name='edit_group'),
]

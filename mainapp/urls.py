from django.urls import path

import mainapp.views as controller


app_name = 'mainapp'

urlpatterns = [
    path('', controller.all_groups, name='index'),
    path('<int:id>/', controller.group, name='group'),
]

from django.urls import path

import mainapp.views as controller


app_name = 'mainapp'

urlpatterns = [
    path('', controller.index, name='index'),
]

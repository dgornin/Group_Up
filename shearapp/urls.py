from django.urls import path
import shearapp.views as controller


app_name = 'shearapp'

urlpatterns = [
    path('<int:id>/<str:key>', controller.index, name='index'),
]

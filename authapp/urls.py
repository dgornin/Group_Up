from django.urls import path

import authapp.views as controller


app_name = 'authapp'

urlpatterns = [
    path('', controller.redirect_to_login, name='index'),
    path('add_sub/<int:id>', controller.add_subscribe, name='add_sub'),
    path('del_sub/<int:id>', controller.del_subscribe, name='del_sub'),
    path('login/', controller.login, name='login'),
    path('logout/', controller.logout, name='logout'),
    path('register/', controller.register, name='register'),
    path('edit/', controller.edit, name='edit'),
    path('profile/<int:id>', controller.profile, name='profile'),
]

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpRequest
from .forms import LoginForm, RegisterForm, UpdateForm
from django.contrib import auth
from django.urls import reverse
from django.conf import settings
from authapp.models import CustomUser, UserSubscribe


# Create your views here.
def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect(reverse('auth:login'))


def login(request: HttpRequest):
    login_form = LoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
    content = {
        'login_form': login_form,
    }
    return render(request, 'authapp/login.html', content)


def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request: HttpRequest):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = RegisterForm()

    content = {
        'reg_form': register_form,
    }

    return render(request, 'authapp/register.html', content)


def edit(request: HttpRequest):
    if request.method == 'POST':
        update_form = UpdateForm(request.POST, instance=request.user)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        update_form = UpdateForm(instance=request.user)

    content = {
        'update_form': update_form,
    }

    return render(request, 'authapp/edit.html', content)


def profile(request: HttpRequest, id: int):
    page_user = CustomUser.objects.filter(id=id)
    user_is_subscribe = False
    if page_user:
        page_user = get_object_or_404(CustomUser, id=id)
        user_is_exists = True
        subscribe = UserSubscribe.objects.filter(user=request.user.id, subscribe=page_user.id)
        if subscribe:
            user_is_subscribe = True
    else:
        user_is_exists = False

    context = {
        'user_is_subscribe': user_is_subscribe,
        'user_is_exists': user_is_exists,
        'page_id': id,
        'page_user': page_user,
    }

    return render(request, 'authapp/profile.html', context)


def add_subscribe(request: HttpRequest, id: int):
    if request.user.is_authenticated:
        id_sub_user = get_object_or_404(CustomUser, id=id)
        is_exist = UserSubscribe.objects.filter(user=request.user.id, subscribe=id_sub_user.id)
        if not is_exist:
            subscriber = UserSubscribe(user=request.user, subscribe=id_sub_user)
            subscriber.save()

    return HttpResponseRedirect(reverse('mainapp:index'))


def del_subscribe(request: HttpRequest, id: int):
    if request.user.is_authenticated:
        id_sub_user = get_object_or_404(CustomUser, id=id)
        is_exist = UserSubscribe.objects.filter(user=request.user.id, subscribe=id_sub_user.id)
        if is_exist:
            subscribe = get_object_or_404(UserSubscribe, user=request.user.id, subscribe=id_sub_user.id)
            subscribe.delete()

    return HttpResponseRedirect(reverse('mainapp:index'))

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest
from .forms import LoginForm, RegisterForm, UpdateForm
from django.contrib import auth
from django.urls import reverse


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

    context = {
        'page_id': id,
    }

    return render(request, 'authapp/profile.html', context)

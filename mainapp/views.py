from django.shortcuts import render
from django.http import HttpRequest
from .models import User

# Create your views here.


def index(request):
    context = {
        'index_isActive': "menu-link-active",
        'contact_isActive': "",
    }
    return render(request, 'mainapp/index.html', context)


def dev(request):
    return render(request, 'mainapp/dev.html')


def contact(request):
    context = {
        'index_isActive': "",
        'contact_isActive': "menu-link-active",
    }
    return render(request, 'mainapp/contact.html', context)

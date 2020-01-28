from django.shortcuts import render
from django.http import HttpRequest
from .models import User

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def dev(request):
    return render(request, 'mainapp/dev.html')


def contact(request):
    return render(request, 'mainapp/contact.html')

from django.shortcuts import render
from django.http import HttpRequest
from .models import User, Group

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def dev(request):
    return render(request, 'mainapp/dev.html')


def all_groups(request):
    return render(request, 'mainapp/all_groups.html')


def group(request, id=None):
    groups = Group.objects.get(pk=id)
    return render(request, 'mainapp/group.html')

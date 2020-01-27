from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from groupsapp.models import Group, Available
from django.urls import reverse

# Create your views here.


def add_user(request: HttpRequest, id: int):
    group = get_object_or_404(Group, pk=id)

    certain_group = Available.objects.filter(groups__id=id)

    if certain_group:
        pass
    else:
        new_available = Available(user=request.user, groups=group)
        new_available.quantity += 1
        new_available.save()

    return HttpResponseRedirect(reverse('groups:index'))


def remove_user(request: HttpRequest, id: int):
    pass


def index(request: HttpRequest):
    group = Available.objects.filter(user=request.user)

    context = {
        'group': group
    }

    return render(request, 'groupsapp/index.html', context)


def group(request: HttpRequest, id: int):
    group = get_object_or_404(Group, pk=id)
    available_groups = get_object_or_404(Available, groups=id)
    a = 123
    a = type(a)

    context = {
        'group': group,
        'available': available_groups,
        'a': a,
    }

    return render(request, 'groupsapp/group.html', context)


def shear(request: HttpRequest, id: int):
    shear_url = f"http://127.0.0.1:8000/groups/add/{id}"

    context = {
        'shear_url': shear_url,
    }

    return render(request, 'groupsapp/shear.html', context)

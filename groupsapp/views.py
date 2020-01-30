from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from groupsapp.models import Group, Available
from django.urls import reverse

# Create your views here.


def add_user(request: HttpRequest, id: int):
    group = get_object_or_404(Group, pk=id)

    certain_group = Available.objects.filter(groups__id=id)

    new_available = Available(user=request.user, groups=group)
    new_available.quantity += 1
    new_available.save()

    return HttpResponseRedirect(reverse('groups:index'))


def remove_user(request: HttpRequest, id: int):
    pass


def index(request: HttpRequest):
    if request.user.is_authenticated:
        group = Available.objects.filter(user=request.user)
        if not group:
            group = False
    else:
        group = False

    context = {
        'group': group
    }

    return render(request, 'groupsapp/index.html', context)


def group(request: HttpRequest, id: int, key: str):
    # available_groups = get_object_or_404(Available, groups=id, user=request.user.id)
    uuid = True
    if request.user.is_authenticated:
        available_groups = Available.objects.filter(groups=id, user=request.user.id)
        if not available_groups:
            group = False
        else:
            group = get_object_or_404(Group, pk=id)
            if str(group.uuid) != key:
                group = False
                uuid = False
            else:
                uuid = group.uuid
    else:
        group = False
        available_groups = False

    context = {
        'group': group,
        'available': available_groups,
        'uuid': uuid,
    }

    return render(request, 'groupsapp/group.html', context)


def shear(request: HttpRequest, id: int):
    shear_url = f"http://127.0.0.1:8000/groups/add/{id}"

    context = {
        'shear_url': shear_url,
    }

    return render(request, 'groupsapp/shear.html', context)

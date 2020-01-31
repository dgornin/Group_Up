from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from groupsapp.models import Group, Available
from django.urls import reverse
from groupsapp.forms import GroupEditForm

# Create your views here.


def add_user(request: HttpRequest, id: int, key: str):
    if request.user.is_authenticated:
        group = get_object_or_404(Group, pk=id)

        certain_group = Available.objects.filter(groups__id=id, user=request.user)

        if certain_group:
            pass
        else:
            if key == str(group.uuid):
                new_available = Available(user=request.user, groups=group)
                new_available.quantity += 1
                new_available.save()

    return HttpResponseRedirect(reverse('groups:index'))


def remove_user(request: HttpRequest, id: int, key: str):
    if request.user.is_authenticated:
        able = get_object_or_404(Available, groups=id, user=request.user)
        if str(able.groups.uuid) == key:
            able.delete()

    return HttpResponseRedirect(reverse('groups:index'))


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
    all_users = False
    if request.user.is_authenticated:
        available_groups = Available.objects.filter(groups=id, user=request.user.id)
        all_users = Available.objects.filter(groups=id)
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
        'all_users': all_users,
    }

    return render(request, 'groupsapp/group.html', context)


def new_group(request: HttpRequest):
    if request.method == 'POST':
        group_form = GroupEditForm(request.POST, request.FILES)
        if group_form.is_valid():
            data = group_form.cleaned_data.get("uuid")
            group_form.save()
            able = get_object_or_404(Group, uuid=data)
            new_available = Available(user=request.user, groups=able)
            new_available.quantity += 1
            new_available.save()
            return HttpResponseRedirect(reverse('groups:index'))
    else:
        group_form = GroupEditForm()

    context = {
        'group_form': group_form
    }

    return render(request, 'groupsapp/new_group.html', context)

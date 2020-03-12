from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from groupsapp.models import Group, Available, Task
from django.urls import reverse
from groupsapp.forms import GroupEditForm, TaskEditForm

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
        'group_form': group_form,
    }

    return render(request, 'groupsapp/new_group.html', context)


def task(request: HttpRequest, id: int, key: str):
    authenticated = False
    user_is_valid = False
    group_is_valid = False
    task_is = None
    if request.user.is_authenticated:
        authenticated = True
        available_group = Group.objects.filter(uuid=key)
        if available_group:
            group_is_valid = True
            available_group = get_object_or_404(Group, uuid=key)
            available_user = Available.objects.filter(user=request.user.id, groups=available_group.id)
            if available_user:
                user_is_valid = True
                task_is = Task.objects.filter(id=id, group=available_group.id)
                if task:
                    task_is = get_object_or_404(Task, id=id, group=available_group.id)

    context = {
        'task': task_is,
        'authenticated': authenticated,
        'group_is_valid': group_is_valid,
        'user_is_valid': user_is_valid,
    }

    return render(request, 'groupsapp/task.html', context)


def all_tasks(request: HttpRequest, key: str):
    authenticated = False
    key_is_valid = False
    user_is_valid = False
    tasks = None
    group_is = None
    if request.user.is_authenticated:
        authenticated = True
        group_is = Group.objects.filter(uuid=key)
        if group_is:
            key_is_valid = True
            group_is = get_object_or_404(Group, uuid=key)
            available = Available.objects.filter(user=request.user.id, groups=group_is.id)
            if available:
                user_is_valid = True
                tasks = Task.objects.filter(group=group_is.id)

    context = {
        'authenticated': authenticated,
        'key_is_valid': key_is_valid,
        'user_is_valid': user_is_valid,
        'tasks': tasks,
        'group_is': group_is,
    }

    return render(request, 'groupsapp/all_tasks.html', context)


def new_task(request: HttpRequest, id: int):
    task_form = None
    authenticated = False
    user_is_valid = False
    if request.user.is_authenticated:
        authenticated = True
        available = Available.objects.filter(user=request.user.id, groups=id)
        if available:
            user_is_valid = True
            if request.method == 'POST':
                task_form = TaskEditForm(request.POST, request.FILES)
                if task_form.is_valid():
                    task_form.group = id
                    task_form.save()
                    return HttpResponseRedirect(reverse('groups:index'))
            else:
                task_form = TaskEditForm(initial={'is_done': False, 'group': id})

    context = {
        'task_form': task_form,
        'authenticated': authenticated,
        'user_is_valid': user_is_valid,
    }

    return render(request, 'groupsapp/new_task.html', context)

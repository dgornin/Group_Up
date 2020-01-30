from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request: HttpRequest, id: int, key: str):
    shear_url = f"http://127.0.0.1:8000/groups/add/{id}/{key}"

    context = {
        'shear_url': shear_url,
    }

    return render(request, 'shearapp/index.html', context)

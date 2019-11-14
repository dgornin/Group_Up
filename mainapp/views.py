from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def dev(request):
    return render(request, 'mainapp/dev.html')

from django.shortcuts import render


def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)


def index(request):
    user_info = {'name': 'Chris'}
    return render(request, 'index.html', user_info)

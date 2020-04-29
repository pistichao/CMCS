from django.shortcuts import render
from DataBase.models import Users, Cars, Tasks


def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)


def index(request):
    user_info = {'name': 'Chris'}
    return render(request, 'index.html', user_info)


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        fname = email.split('@', 1)[0]
        pswd = request.POST.get('password')
        message = "Please check your username or password."
        if email.strip() and pswd:
            # todo:validate email and password prototype
            try:
                user = Users.objects.get(firstname=fname)
                if user.password == pswd:
                    return render(request, 'user.html', {'name': user.username})
                return render(request, 'login.html', {'message': message})
            except:
                message = "User didn't exist!"
                return render(request, 'login.html', {'message': message})
        else:
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html', )


def notfound(request):
    return render(request, '404.html')

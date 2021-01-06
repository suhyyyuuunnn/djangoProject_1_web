from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from posts.models import Post


def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create(
                username=request.POST["username"],
                password=request.POST["password"],
                email=request.POST["email"]
            )
            auth.login(request, user)
            return redirect('login.html')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'posts:main')
        else:
            return render(request, 'users/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    context = {
        'posts': Post.objects.order_by('-created_at')
    }
    return render(request, 'posts:main', context)
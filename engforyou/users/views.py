from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверные данные')
    return render(request, 'users/login.html')
        
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь уже существует')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Аккаунт успешно создан')
            return redirect('users:login')
    return render(request, 'users/register.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

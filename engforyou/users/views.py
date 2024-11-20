from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

from .forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name =  'users/login.html'
    
    
 
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    def get_success_url(self):
        path = self.request.GET.get('path')
        if path:
            return f"{reverse_lazy('users:login')}?next={path}"
        return reverse_lazy('users:login')
        
def register1(request):
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

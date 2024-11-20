from django.contrib.auth import logout, get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse, reverse_lazy

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


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
    
class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

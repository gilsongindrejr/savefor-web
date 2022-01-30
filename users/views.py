from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class LoginUserView(LoginView):
    template_name = 'users/login.html'


class LogoutUserView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'


class PasswordChangeUserView(PasswordChangeView):
    template_name = 'users/password_change.html'


class RegisterUserView(CreateView):
    template_name = 'users/register.html'
    model = get_user_model()
    success_url = reverse_lazy('users:login')
    form_class = CustomUserCreationForm

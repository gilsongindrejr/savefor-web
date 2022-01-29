from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginUserView(LoginView):
    template_name = 'users/login.html'


class LogoutUserView(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'


class PasswordChangeUserView(PasswordChangeView):
    template_name = 'users/password_change.html'
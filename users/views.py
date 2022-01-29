from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView


class LoginView(LoginView):
    template_name = 'users/login.html'


class LoginView(LogoutView):
    template_name = 'users/logout.html'


class PasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
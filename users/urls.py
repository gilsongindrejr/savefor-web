from django.urls import path

from .views import LoginUserView, LogoutUserView, PasswordChangeUserView, RegisterUserView
from .forms import UserLoginForm

app_name = 'users'
urlpatterns = [
    path('login', LoginUserView.as_view(authentication_form=UserLoginForm), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('password_change', PasswordChangeUserView.as_view(success_url='login'), name='password_change'),
    path('register', RegisterUserView.as_view(), name='register'),
]

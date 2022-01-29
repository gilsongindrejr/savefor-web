from django.urls import path

from users.views import LoginUserView, LogoutUserView, PasswordChangeUserView

app_name = 'users'
urlpatterns = [
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('password_change', PasswordChangeUserView.as_view(success_url='login'), name='password_change'),
]

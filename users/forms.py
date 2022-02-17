from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.utils.translation import gettext as _


class CustomPasswordChangeForm(PasswordChangeForm):
    # Overriden to get rid of help text and change the classes
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'l-margin-bottom-1em c-form-box', 'placeholder': 'Old password', 'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'class': 'l-margin-bottom-1em c-form-box', 'placeholder': 'New password', 'autocomplete': 'new-password'}),
        strip=False,
        help_text=None,
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'l-margin-bottom-1em c-form-box', 'placeholder': 'New password confirmation', 'autocomplete': 'new-password'}),
    )


class CustomUserCreationForm(UserCreationForm):

    error_messages = {
        'password_too_short': 'The password must contain at least %(min_length)d character.'
    }

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': '',
            'email': ''
        }
        help_texts = {
            'username': None
        }
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'l-margin-bottom-1em c-form-box', 'placeholder': 'Username'}
            ),
            'email': forms.TextInput(
                attrs={'class': 'l-margin-bottom-1em c-form-box', 'placeholder': 'Email'}
            )
        }

    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'l-margin-bottom-1em c-form-box',
                   'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password',
                   'class': 'l-margin-bottom-1em c-form-box',
                   'placeholder': 'Password confirmation'}),
        strip=False,
    )


class UserLoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label='', widget=forms.TextInput(attrs={'class': 'l-margin-bottom-1em c-form-box', 'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'l-margin-bottom-1em c-form-box', 'placeholder': 'Password'}))

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password."
        ),
        'inactive': _("This account is inactive."),
    }

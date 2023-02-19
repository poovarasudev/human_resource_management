from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='',
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'class': 'form-control form-control-lg',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control form-control-lg',
            'placeholder': 'Password'
        })
    )


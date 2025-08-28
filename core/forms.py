from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

STYLE_CLASS = 'w-full py-4 px-6 rounded-xl'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': STYLE_CLASS}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': STYLE_CLASS}))


class SinupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Your username', 'class': STYLE_CLASS}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email address', 'class': STYLE_CLASS}),
        }
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': STYLE_CLASS}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'class': STYLE_CLASS}))
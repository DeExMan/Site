from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['club'].empty_label = "Клуб не выбран"

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'club', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ChangeUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['club'].empty_label = "Клуб не выбран"

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'club')


class AddClubForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Club
        fields = (['name'])
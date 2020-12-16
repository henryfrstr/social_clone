from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Display name')
    email = forms.EmailField(label='Email Address')

    class Meta:
        fields = ('username', 'email')
        model = User

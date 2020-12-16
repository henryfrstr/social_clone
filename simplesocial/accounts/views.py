from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


class UserRegister(CreateView):
    form_class = forms.UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = "accounts/register.html"

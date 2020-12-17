from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import Group


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    model = Group
    fields = ('name', 'description')


class SingleGroup(generic.DetailView):
    model = Group
    
class ListGroup(generic.ListView):
    model = Group
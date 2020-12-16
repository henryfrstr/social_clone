from django.db import models
from django.contrib.auth.models import User


def get_name(self):
    return "@{}".format(self.username)


User.add_to_class("__str__", get_name)

# Create your models here.

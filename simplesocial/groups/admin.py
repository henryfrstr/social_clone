from django.contrib import admin
from . import models


class GruopMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)

# Register your models here.

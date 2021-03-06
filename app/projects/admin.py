from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": AdminMartorWidget},
    }


admin.site.register(Project, ProjectAdmin)

# Register your models here.

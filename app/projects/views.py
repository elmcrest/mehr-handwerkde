from django.views.generic import ListView
from .models import Project


class ProjectListView(ListView):
    class Meta:
        model = Project

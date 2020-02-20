from django.views.generic import TemplateView
from projects.models import Project


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["highlights"] = Project.objects.filter(highlight=True)
        return ctx


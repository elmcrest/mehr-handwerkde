from django.db import models
from martor.models import MartorField


class Project(models.Model):
    name = models.CharField("Name", help_text="Ein schöner Projektname.", max_length=30)
    date = models.DateField("Datum")
    content = MartorField("Inhalt", help_text="Markdown Quelltext")

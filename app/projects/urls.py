from django.urls import path, re_path
from .views import markdown_uploader

urlpatterns = [
    path("api/uploader/", markdown_uploader, name="markdown_uploader_page"),
]

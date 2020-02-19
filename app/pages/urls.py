from django.urls import path, re_path
from .views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("leitbild", IndexView.as_view(), name="leitbild"),
    path("jobs", IndexView.as_view(), name="jobs"),
]

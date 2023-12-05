from django.urls import include, path

from . import views

app_name = "judge"

urlpatterns = [
    path("judges/", views.judges, name="judges"),
]

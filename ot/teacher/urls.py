from django.urls import include, path

from . import views

app_name = "teacher"

urlpatterns = [
    path("teachers/", views.teachers, name="teachers"),
]

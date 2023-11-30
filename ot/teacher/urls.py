from django.urls import include, path

from . import views

app_name = "teacher"

urlpatterns = [
    path("list/", views.teacher_list, name="teacher_list"),
]

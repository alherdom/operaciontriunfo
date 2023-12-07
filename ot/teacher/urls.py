from django.urls import include, path

from . import views

app_name = "teacher"

urlpatterns = [
    path("teachers/", views.teachers, name="teachers"),
    path("teachers/<slug:teacher_slug>/", views.teacher_detail, name="teacher_detail"),
]

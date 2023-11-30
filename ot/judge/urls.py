from django.urls import include, path

from . import views

app_name = "judge"

urlpatterns = [
    path("list/", views.judge_list, name="judge_list"),
]

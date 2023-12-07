from django.urls import include, path

from . import views

app_name = "judge"

urlpatterns = [
    path("judges/", views.judges, name="judges"),
    path("judges/<slug:judge_slug>/", views.judge_detail, name="judge_detail"),
]

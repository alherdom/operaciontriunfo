from django.urls import include, path

from . import views

app_name = "contestant"

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.contestant_list, name="contestant_list"),
]

from django.urls import include, path

from . import views

app_name = "contestant"

urlpatterns = [
    path("", views.index, name="index"),
    path("contestants/", views.contestants, name="contestants"),
]

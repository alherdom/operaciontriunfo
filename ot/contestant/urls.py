from django.urls import include, path

from . import views

app_name = "contestant"

urlpatterns = [
    path("", views.index, name="index"),
    path("contestants/", views.contestants, name="contestants"),
    path("contestant/<slug:contestant_slug>/", views.contestant_detail, name="contestant_detail"),
    path("search/", views.search, name="search"),
]

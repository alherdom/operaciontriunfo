from django.contrib import admin
from .models import MusicStyle, Contestant


@admin.register(Contestant)
class ContestantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "avatar",
        "slug",
        "birthdate",
        "city",
        "job",
        "hobbies",
        "nationality",
        "music_style",
        "role",
    ]
    list_editable = [
        "first_name",
        "last_name",
        "avatar",
        "slug",
        "birthdate",
        "city",
        "job",
        "hobbies",
        "nationality",
        "music_style",
        "role",
    ]
    prepopulated_fields = dict(slug=("first_name", "last_name"))


@admin.register(MusicStyle)
class MusicStyleAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_editable = ["name", "slug"]
    prepopulated_fields = dict(slug=("name",))

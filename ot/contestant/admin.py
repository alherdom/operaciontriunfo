from django.contrib import admin
from .models import MusicStyle, Contestant


@admin.register(Contestant)
class ContestantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "slug",
        "birthdate",
        "city",
        "job",
        "hobbies",
        "nationality",
        "avatar",
        "music_style",
    ]
    list_editable = [
        "first_name",
        "last_name",
        "slug",
        "birthdate",
        "city",
        "job",
        "hobbies",
        "nationality",
        "avatar",
        "music_style",
    ]
    prepopulated_fields = dict(slug=("first_name", "last_name"))


@admin.register(MusicStyle)
class MusicStyleAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_editable = ["name", "slug"]
    prepopulated_fields = dict(slug=("name",))

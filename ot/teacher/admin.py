from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "avatar",
        "slug",
        "subject",
        "description",
        "role",
    ]
    list_editable = [
        "first_name",
        "last_name",
        "avatar",
        "slug",
        "subject",
        "description",
        "role",
    ]
    prepopulated_fields = dict(slug=("first_name", "last_name"))

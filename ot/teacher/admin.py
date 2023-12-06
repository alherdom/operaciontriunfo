from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "avatar", "slug", "subject", ]
    list_editable = ["first_name", "last_name","avatar", "slug", "subject"]
    prepopulated_fields = dict(slug=("first_name", "last_name"))

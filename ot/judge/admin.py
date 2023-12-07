from django.contrib import admin

from .models import Judge


@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "avatar",
        "slug",
        "job",
        "description",
    ]
    list_editable = ["first_name", "last_name", "avatar", "slug", "job", "description"]
    prepopulated_fields = dict(slug=("first_name", "last_name"))

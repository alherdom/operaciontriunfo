from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    subject = models.CharField(max_length=20)
    avatar = models.ImageField()
    description = models.CharField(max_length=600)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["first_name"])]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.subject}"

    def get_absolute_url(self) -> str:
        return reverse("teacher:teacher_detail", kwargs=dict(teacher_slug=self.slug))

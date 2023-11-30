from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    subject = models.CharField(max_length=20)
    avatar = models.ImageField()

    class Meta:
        ordering = ["first_name"]
        indexes = [models.Index(fields=["first_name"])]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.subject}"

from django.db import models

from django.urls import reverse


class MusicStyle(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Contestant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    birthdate = models.DateField()
    city = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    hobbies = models.CharField(max_length=250)
    nationality = models.CharField(max_length=50)
    avatar = models.ImageField()
    music_style = models.ForeignKey(MusicStyle, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

    class Meta:
        ordering = ["first_name"]
        indexes = [models.Index(fields=["first_name"])]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self) -> str:
        return reverse(
            "contestant:contestant_detail", kwargs=dict(contestant_slug=self.slug)
        )

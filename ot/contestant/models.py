from django.db import models


class MusicStyle(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)


class Contestant(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    birthdate = models.DateField()
    city = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    hobbies = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    avatar = models.ImageField()
    music_style = models.ForeignKey(MusicStyle, on_delete=models.CASCADE)

    class Meta:
        ordering = ["first_name"]
        indexes = [models.Index(fields=["first_name"])]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

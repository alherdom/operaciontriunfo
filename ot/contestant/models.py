from django.db import models


class Contestant(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

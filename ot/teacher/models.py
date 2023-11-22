from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    function = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}, {self.function}"

from django.db import models
from django.urls import reverse

class Judge(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)
    job = models.CharField(max_length=20)
    avatar = models.ImageField()
    description = models.CharField(max_length=1000)

    class Meta:
        ordering = ["id"]
        indexes = [models.Index(fields=["first_name"])]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.job}"

    def get_absolute_url(self) -> str:
        return reverse("judge:judge_detail", kwargs=dict(judge_slug=self.slug))
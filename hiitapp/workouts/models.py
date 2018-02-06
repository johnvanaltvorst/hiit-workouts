from django.db import models
from django.urls import reverse

# Create your models here.

class Workout(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workouts:list")

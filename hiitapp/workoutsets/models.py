from django.db import models
from django.urls import reverse

from workouts.models import Workout
from workoutvideos.models import WorkoutVideo

# Create your models here.
class WorkoutSet(models.Model):
    name = models.CharField(max_length=255)
    workout = models.ForeignKey(Workout, related_name="workoutsets", on_delete=models.CASCADE)
    video = models.ForeignKey(WorkoutVideo, related_name="workoutsets", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        # return reverse("workouts:detail",kwargs={"pk": self.kwargs.get("pk")})
        # return reverse('workouts:detail', pk=self.kwargs['pk'])

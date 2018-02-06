from django.db import models
from django.urls import reverse

from workoutsets.models import WorkoutSet

# Create your models here.
class ActionSet(models.Model):
    name = models.CharField(max_length=255)
    workoutset = models.ForeignKey(WorkoutSet, related_name="actionsets", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_absolute_url(self): #this works.  if uncoommenting this, then comment out get_success_url in views
    #     return reverse('workouts:workoutset_single', args=[self.workoutset_id])

from django.db import models
from django.urls import reverse

from actionsets.models import ActionSet

# Create your models here.
class Action(models.Model):
    action_type = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField()
    actionset = models.ForeignKey(ActionSet, related_name="actions", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "action_type: {}, duration: {}".format(self.action_type, self.duration)

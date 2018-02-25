from django.db import models
from django.urls import reverse


# Create your models here.
class WorkoutVideo(models.Model):
    name = models.CharField(max_length=255)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

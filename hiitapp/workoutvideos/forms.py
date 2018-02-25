from django import forms
from django.forms import ModelForm
from .models import WorkoutVideo

class VideoForm(forms.ModelForm):
    class Meta:
        model = WorkoutVideo
        fields = ["name", "videofile"]

from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)

from .models import WorkoutVideo
from workoutsets.models import WorkoutSet

# Create your views here.
class WorkoutVideoListView(ListView):
    model = WorkoutVideo

class WorkoutVideoDetailView(DetailView):
    model = WorkoutVideo

class WorkoutVideoCreateView(CreateView):
    model = WorkoutVideo
    fields = ('name',)

    def get_success_url(self):
        return reverse('workoutvideos:list')

class WorkoutVideoUpdateView(UpdateView):
    model = WorkoutVideo
    fields = ('name',)

    def get_success_url(self):
        return reverse('workoutvideos:list')

class WorkoutVideoDeleteView(DeleteView):
    model = WorkoutVideo

    def get_success_url(self):
        return reverse('workouts:list')

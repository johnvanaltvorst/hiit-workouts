from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)

from .models import WorkoutSet, WorkoutVideo
from workouts.models import Workout

# Create your views here.
class WorkoutSetListView(ListView):
    model = WorkoutSet

class WorkoutSetDetailView(DetailView):
    model = WorkoutSet

class WorkoutSetCreateView(CreateView):
    model = WorkoutSet
    fields = ('name','workout','video',)

    def get_initial(self):
        workout = get_object_or_404(Workout, pk=self.kwargs.get('pk'))
        return {
            'workout':workout,
        }

    def get_success_url(self):
        return reverse('workouts:detail',kwargs={'pk':self.kwargs['pk']})

class WorkoutSetUpdateView(UpdateView):
    model = WorkoutSet
    fields = ('name','workout','video')

    def get_success_url(self):
        return reverse('workouts:list')

class WorkoutSetDeleteView(DeleteView):
    model = WorkoutSet

    def get_success_url(self):
        return reverse('workouts:list')

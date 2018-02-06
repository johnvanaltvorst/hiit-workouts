from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)

from .models import ActionSet
from workoutsets.models import WorkoutSet

# Create your views here.
class ActionSetListView(ListView):
    model = ActionSet

class ActionSetDetailView(DetailView):
    model = ActionSet

class ActionSetCreateView(CreateView):
    model = ActionSet
    fields = ('name','workoutset',)

    def get_initial(self):
        workoutset = get_object_or_404(WorkoutSet, pk=self.kwargs.get('pk'))
        return {
            'workoutset':workoutset,
        }

    def get_success_url(self):
        return reverse('workouts:list')

class ActionSetUpdateView(UpdateView):
    model = ActionSet
    fields = ('name','workoutset',)

    def get_success_url(self):
        return reverse('workouts:list')

class ActionSetDeleteView(DeleteView):
    model = ActionSet

    def get_success_url(self):
        return reverse('workouts:list')

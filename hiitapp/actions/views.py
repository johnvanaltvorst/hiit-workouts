from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)

from .models import Action
from actionsets.models import ActionSet

# Create your views here.
class ActionListView(ListView):
    model = Action

class ActionDetailView(DetailView):
    model = Action

class ActionCreateView(CreateView):
    model = Action
    fields = ('action_type','duration','actionset',)

    def get_initial(self):
        actionset = get_object_or_404(ActionSet, pk=self.kwargs.get('pk'))
        return {
            'actionset':actionset,
        }

    def get_success_url(self):
        return reverse('workouts:list')

class ActionUpdateView(UpdateView):
    model = Action
    fields = ('action_type','duration','actionset')

    def get_success_url(self):
        return reverse('workouts:list')

class ActionDeleteView(DeleteView):
    model = Action

    def get_success_url(self):
        return reverse('workouts:list')

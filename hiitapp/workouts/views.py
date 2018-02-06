from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from django.core import serializers
from django.http import JsonResponse
from braces.views import SelectRelatedMixin

from .models import Workout
from workoutsets.models import WorkoutSet
from actions.models import Action
# Create your views here.

def actionsAPI(self,actionset_pk):
    actions_json = serializers.serialize('json', Action.objects.filter(actionset_id=actionset_pk))
    return JsonResponse(actions_json)


class WorkoutListView(ListView):
    model = Workout

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action_json"] = serializers.serialize('json', Action.objects.all())
        return context

class WorkoutDetailView(DetailView):
    model = Workout

class WorkoutCreateView(CreateView):
    model = Workout
    fields = ('name',)

class WorkoutDeleteView(DeleteView):
    model = Workout
    success_url = reverse_lazy('workouts:list')

class WorkoutUpdateView(UpdateView):
    model = Workout
    fields = ('name',)

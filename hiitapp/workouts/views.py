from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView, TemplateView)
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

class WorkoutPlayView(TemplateView):
    template_name = 'workouts/index.html'
    model = Workout

    def get_context_data(self,**kwargs):
        workout = Workout.objects.get(id=self.kwargs['workout_pk'])

        if('workoutset_pk' in self.kwargs):
            next_workoutset = (WorkoutSet.objects.filter(workout_pk=self.kwargs['workout_pk'])
                                        .filter(workoutset_pk__gt=self.kwargs['workoutset_pk'])
                                        .order_by('pk')[0:1])
        else:
            next_workoutset = (WorkoutSet.objects.filter(workout_id=self.kwargs['workout_pk'])
                                        .order_by('pk')[0:1])
        context = super().get_context_data(**kwargs)
        context['workout'] = workout
        context['next_workoutset'] = next_workoutset
        # context['workoutsets'] = WorkoutSet.objects.filter(workout_id=self.kwargs['pk'])
        return context

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

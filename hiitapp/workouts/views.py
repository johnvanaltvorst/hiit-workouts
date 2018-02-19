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
from workoutvideos.models import WorkoutVideo
from actions.models import Action
# Create your views here.

def GetActionsAPI(self,workoutset_id):
    actions_json = Action.objects.filter(actionset__workoutset__id=workoutset_id)
    return JsonResponse(serializers.serialize('json', actions_json), safe=False)

def GetVideoAPI(self,workoutset_pk):
    workoutset = WorkoutSet.objects.get(id=workoutset_pk)
    video = WorkoutVideo.objects.filter(id=workoutset.video.id)
    video_json = serializers.serialize('json', video)
    return JsonResponse(video_json, safe=False)

class WorkoutPlayView(TemplateView):
    template_name = 'workouts/play.html'
    model = Workout

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        workout = Workout.objects.get(id=self.kwargs['workout_pk'])

        next_workoutset_exists = False

        print("before if")
        if('workoutset_pk' in self.kwargs): #used on PLAY NEXT WORKOUTSET
            print("in if")

            context['current_workoutset'] = (WorkoutSet.objects
                                                    .filter(workout=workout)
                                                    .filter(id__gt=self.kwargs['workoutset_pk'])
                                                    .first())

            context['current_actions'] = (Action.objects
                                                    .filter(actionset__workoutset__id=self.kwargs['workoutset_pk'])
                                                    .order_by('id'))

            actions = (Action.objects
                             .filter(actionset__workoutset__id=self.kwargs['workoutset_pk']))

            timesets = []
            for action in actions:
                timesets.append({"type":action.action_type,"duration":action.duration})

            context['timesets'] = timesets

            next_workoutset_qs = (WorkoutSet.objects.filter(workout_id=self.kwargs['workout_pk'])
                                        .filter(id__gt=self.kwargs['workoutset_pk'])
                                        .order_by('pk'))

            if(next_workoutset_qs):
                print("test")
                print(next_workoutset_qs)
                context['next_workoutset_pk'] = next_workoutset_qs.first()
                next_workoutset_exists = True

        else: #used on PLAY ON WORKOUT LIST PAGE (only workout_id given)
            print("in else")
            context['current_workoutset'] = WorkoutSet.objects.filter(workout=workout).first()

            actions = (Action.objects
                             .filter(actionset__workoutset__workout=workout))

            timesets = []
            for action in actions:
                timesets.append({"type":str(action.action_type),"duration":action.duration})

            context['timesets'] = timesets

            next_workoutset_pk = (WorkoutSet.objects.filter(workout_id=self.kwargs['workout_pk'])
                                        .order_by('pk')[1])

            if(next_workoutset_pk):
                context['next_workoutset_pk'] = next_workoutset_pk.id
                next_workoutset_exists = True

        context['workout'] = workout
        context['next_workoutset_exists'] = next_workoutset_exists
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

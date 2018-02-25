from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)

from .models import WorkoutVideo
from .forms import VideoForm
from workoutsets.models import WorkoutSet

# Create your views here.

def play(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request,'workoutvideos/index.html',context_dict)

def uploadvideo(request):

    lastvideo = WorkoutVideo.objects.last()

    videofile = lastvideo.videofile

    form = VideoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context = {'videofile': videofile,
              'form': form
              }

    return render(request, 'workoutvideos/videos.html', context)

class WorkoutVideoListView(ListView):
    model = WorkoutVideo

class WorkoutVideoDetailView(DetailView):
    model = WorkoutVideo

class WorkoutVideoCreateView(CreateView):
    model = WorkoutVideo
    fields = ('name','videofile')

    def get_success_url(self):
        return reverse('workoutvideos:list')

class WorkoutVideoUpdateView(UpdateView):
    model = WorkoutVideo
    fields = ('name','videofile')

    def get_success_url(self):
        return reverse('workoutvideos:list')

class WorkoutVideoDeleteView(DeleteView):
    model = WorkoutVideo

    def get_success_url(self):
        return reverse('workouts:list')

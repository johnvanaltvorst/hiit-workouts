from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    path('', views.WorkoutListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.WorkoutDetailView.as_view(), name='detail'),
    path('new/', views.WorkoutCreateView.as_view(), name='new'),
    path('delete/<int:pk>/', views.WorkoutDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.WorkoutUpdateView.as_view(), name='update'),
    path('actionsAPI/workoutset/<int:workoutset_id>/', views.GetActionsAPI, name='api_get_actions'),
    path('play/workout/<int:workout_pk>/', views.WorkoutPlayView.as_view(), name='play_initial'),
    path('play/workout/<int:workout_pk>/workoutset/<int:workoutset_pk>/', views.WorkoutPlayView.as_view(), name='play_next'),
    path('api/video/for/workoutset/<int:workoutset_pk>/', views.GetVideoAPI, name='api_get_video'),
]

from django.urls import path
from . import views

app_name = 'workoutvideos'

urlpatterns = [
    path('', views.WorkoutVideoListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.WorkoutVideoDetailView.as_view(), name='detail'),
    path('new/', views.WorkoutVideoCreateView.as_view(), name='new'),
    path('delete/<int:pk>/', views.WorkoutVideoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.WorkoutVideoUpdateView.as_view(), name='update'),

]

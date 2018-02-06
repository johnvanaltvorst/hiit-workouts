from django.urls import path
from . import views

app_name = 'workoutsets'

urlpatterns = [
    path('', views.WorkoutSetListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.WorkoutSetDetailView.as_view(), name='detail'),
    path('new/', views.WorkoutSetCreateView.as_view(), name='new'),
    path('delete/<int:pk>/', views.WorkoutSetDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.WorkoutSetUpdateView.as_view(), name='update'),
    path('add/to/workout/<int:pk>/', views.WorkoutSetCreateView.as_view(), name='add_to_workout'),
]

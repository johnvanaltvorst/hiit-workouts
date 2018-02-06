from django.urls import path
from . import views

app_name = 'actionsets'

urlpatterns = [
    path('', views.ActionSetListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ActionSetDetailView.as_view(), name='detail'),
    path('new/', views.ActionSetCreateView.as_view(), name='new'),
    path('delete/<int:pk>/', views.ActionSetDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.ActionSetUpdateView.as_view(), name='update'),
    path('add/to/workoutset/<int:pk>/', views.ActionSetCreateView.as_view(), name='add_to_workoutset'),
]

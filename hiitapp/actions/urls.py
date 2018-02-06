from django.urls import path
from . import views

app_name = 'actions'

urlpatterns = [
    path('', views.ActionListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ActionDetailView.as_view(), name='detail'),
    path('new/', views.ActionCreateView.as_view(), name='new'),
    path('delete/<int:pk>/', views.ActionDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.ActionUpdateView.as_view(), name='update'),
    path('add/to/actionset/<int:pk>/', views.ActionCreateView.as_view(), name='add_to_actionset'),
]

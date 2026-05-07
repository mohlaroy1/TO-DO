from django.urls import path
from .views import HomeView, TaskUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),

]
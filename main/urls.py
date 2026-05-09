from django.urls import path
from .views import HomeView, TaskUpdateView, delete_task

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', delete_task, name='delete-task'),

]
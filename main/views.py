from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

class HomeView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def get(self, request):
        statuses = [status[0] for status in STATUS]
        tasks = Task.objects.filter(user=request.user)

        context = {
            'statuses': statuses,
            'tasks': tasks,

        }
        return render(request, 'index.html', context)


    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            details=request.POST['details'],
            status=request.POST['status'],
            deadline=request.POST['deadline'] if request.POST['deadline'] else None,
            user=request.user,
        )
        return self.get(request)


class TaskUpdateView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, pk=pk, user=request.user)
            statuses = [status[0] for status in STATUS]
            context = {
                'task': task,
                'statuses': statuses,
            }
            return render(request, 'edit.html', context)
        return redirect('login')

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.title = request.POST['title']
        task.details = request.POST['details']
        task.status = request.POST['status']
        task.save()
        return redirect('home')

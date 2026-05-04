from django.shortcuts import render
from django.views import View


from .models import *

class HomeView(View):
    def get(self, request):
        statuses=[status[0] for status in STATUS]
        context = {
            'statuses': statuses,

        }
        return render(request, 'index.html', context)

    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            details=request.POST['details'],
            status=request.POST['status'],
            deadline=request.POST['deadline'],
        )
        return self.get(request)
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user=User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
        )
        login(request, user)
        return redirect('home')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user=authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.warning(request, 'Username OR password is incorrect')
        return self.get(request)


def logout_view(request):
    logout(request)
    return redirect('login')

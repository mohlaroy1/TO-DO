from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#class RegisterView(View):
#    def get(self, request):
#        return render(request, 'register.html')
#
#    def post(self, request):
#        user=User.objects.create_user(
#            username = request.POST['username'],
#            password = request.POST['password'],
#       )
#        login(request, user)
#        return redirect('home')



class LoginView(View):

    def post(self, request):
        user=authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.warning(request, 'Username OR password is incorrect')
        return redirect('auth')


def logout_view(request):
    logout(request)
    return redirect('auth')


def auth_view(request):
    return render(request, 'auth.html')


class RegisterView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password-repeat']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if password == password2:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        email=email
                    )
                    login(request, user)
                    return redirect('home')
                messages.error(request, "Parollar mos emas!")
                return redirect('auth')
            messages.error(request, "Ushbu emailda allaqachon hisob mavjud!")
            return redirect('auth')
        messages.error(request, "Foydalanuvchi nomi band!")
        return redirect('auth')


class MyAccountView(LoginRequiredMixin, View):
    login_url = 'auth'
    def get(self, request):
        return render(request, 'profile.html')


class UserUpdateView(LoginRequiredMixin, View):
    login_url = 'auth'

    def post(self, request):
        user=request.user
        user.username = request.POST['username']
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        if request.POST['password'] != '':
            user.set_password(request.POST['password'])
        user.save()
        return redirect('my-account')

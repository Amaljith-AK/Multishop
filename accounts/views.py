import copy

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist. ')
                return redirect('register')
            else:
                Customer = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email,password=password1)
                Customer.save()
                messages.success(request, 'Your Account has been successfully created.')
                return redirect('signin')
        else:
            messages.error(request,'Please check password. ')
            return redirect('register')
    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            name = user.first_name
            return render(request,'index.html')
        else:
            messages.error(request, 'Login Failed')
            return redirect('signin')
    return render(request, 'login.html')



def signout(request):
    logout(request)
    return redirect('/')

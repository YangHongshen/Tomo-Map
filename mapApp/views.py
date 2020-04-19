from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, "mapApp/index.html")


def login(request):
    return HttpResponse("login")


def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, "mapApp/register.html", {'form': form})


def reset_password(request):
    return HttpResponse("register")


def logout(request):
    return HttpResponse("logout")

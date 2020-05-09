from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, "mapApp/index.html")


def login(request):
    return render(request, "mapApp/login.html")


def register(request):
    return render(request, "mapApp/register.html")


def reset(request):
    return render(request, "mapApp/reset.html")


def map(request):
    return render(request, "mapApp/map.html")

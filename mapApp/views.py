from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, "mapApp/index.html")


def login(request):
    '''
    username = request.post['username']
    password = request.post['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "mapApp/login.html")
    '''
    return render(request, "mapApp/login.html")


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


def reset(request):
    return render(request, "mapApp/reset.html")

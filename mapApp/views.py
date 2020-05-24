from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm
from mapApp import models, forms
from django.shortcuts import redirect
from django.contrib import messages


def first_value(dictionary):
    first_key_value = next(iter(dictionary.values()))[0]
    return first_key_value


# Create your views here.

def index_page(request):
    return render(request, "mapApp/index.html")


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "mapApp/login.html", {'form': form})

    def post(self, request):
        form = forms.LoginForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index_page')
        else:
            messages.error(request, "Username and Password does not correct")
            return render(request, "mapApp/login.html", {'form': form})


class RegisterView(View):
    def get(self, request):
        form = UserForm()
        return render(request, "mapApp/register.html", {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account ' + user + ' has created successfully!')
            return redirect("login_page")


def reset_page(request):
    return render(request, "mapApp/reset.html")


def map_page(request):
    return render(request, "mapApp/map.html")

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate
from mapApp import models, forms
import json


# Create your views here.

def index_page(request):
    return render(request, "mapApp/index.html")


def login_page(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"].strip()
            password = form.cleaned_data["password"]
            try:
                user = models.UserModel.objects.get(email=email)
            except ObjectDoesNotExist:
                return render(request, "mapApp/login.html", {'email_messages': ["User not found"], 'form': form})
            if user.password == password:
                return HttpResponse("Congrats, you have logged in successfully")
            else:
                return render(request, "mapApp/login.html",
                              {'password_messages': ["Sorry, passsword is invalid"], 'form': form})
        else:
            messages = form.errors
            try:
                email_messages = messages['email']
            except KeyError:
                email_messages = ""
            try:
                password_messages = messages['password']
            except KeyError:
                password_messages = ""
            return render(request, "mapApp/login.html",
                          {'email_messages': email_messages, 'password_messages': password_messages, 'form': form})
    else:
        form = forms.LoginForm()
        return render(request, "mapApp/login.html", {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 != password2:
                return HttpResponse("Sorry, two password does not match")
            else:
                models.UserModel.objects.create(
                    email=email,
                    password=password1
                )
                return HttpResponse("Congrats, your have registered successfully")
        else:
            return HttpResponse("Sorry, form is invalid")
    else:
        form = forms.RegisterForm()
        return render(request, "mapApp/register.html", {'form': form})


def reset_page(request):
    return render(request, "mapApp/reset.html")


def map_page(request):
    return render(request, "mapApp/map.html")

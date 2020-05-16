from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate
from mapApp import models, forms


def first_value(dictionary):
    first_key_value = next(iter(dictionary.values()))[0]
    return first_key_value


# Create your views here.

def index_page(request):
    return render(request, "mapApp/index.html")


def login_page(request):
    messages = []
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"].strip()
            password = form.cleaned_data["password"]
            try:
                user = models.UserModel.objects.get(email=email)
                if user.password == password:
                    messages.append("Congrats, you have logged in successfully")
                    # TODO: auth system
                else:
                    messages.append("Sorry, passsword is invalid")
            except ObjectDoesNotExist:
                messages.append("User not found")
        else:
            messages.append(first_value(form.errors.values()))
    else:
        form = forms.LoginForm()
    return render(request, "mapApp/login.html", {'messages': messages, 'form': form})


def register_page(request):
    messages = []
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            # TODO: Add complexity check
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 != password2:
                messages.append("Sorry, two password does not match")
            else:
                models.UserModel.objects.create(
                    email=email,
                    password=password1
                )
                messages.append("Congrats, your have registered successfully")
                # TODO: Hop to Login page with auth
        else:
            messages.append(first_value(form.errors))
    else:
        form = forms.RegisterForm()
    return render(request, "mapApp/register.html", {'form': form, 'messages': messages})


def reset_page(request):
    return render(request, "mapApp/reset.html")


def map_page(request):
    return render(request, "mapApp/map.html")

from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.contrib.auth import login, authenticate
from mapApp import models, forms


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
        messages = []
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
            messages.append(first_value(form.errors))
        return render(request, "mapApp/login.html", {'form': form, 'messages': messages})


class RegisterView(View):
    def get(self, request):
        form = forms.RegisterForm()
        return render(request, "mapApp/register.html", {'form': form})

    def post(self, request):
        messages = []
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            # TODO: Add complexity check
            password = form.cleaned_data["password1"]
            models.UserModel.objects.create(
                email=email,
                password=password
            )
            messages.append("Congrats, your have registered successfully")
            # TODO: Hop to Login page with auth
        else:
            messages.append(first_value(form.errors))
        return render(request, "mapApp/register.html", {'form': form, 'messages': messages})


def reset_page(request):
    return render(request, "mapApp/reset.html")


def map_page(request):
    return render(request, "mapApp/map.html")

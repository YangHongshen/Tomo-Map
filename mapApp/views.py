from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from mapApp import models, forms


# Create your views here.

def index_page(request):
    return render(request, "mapApp/index.html")


def login_page(request):
    return render(request, "mapApp/login.html")


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

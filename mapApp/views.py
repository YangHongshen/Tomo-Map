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
        register_email = request.POST.get("register_email", None)
        print(register_email)
        register_password1 = request.POST.get("register_password1", None)
        print(register_password1)
        register_password2 = request.POST.get("register_password2", None)
        print(register_password2)
        if register_password1 != register_password2:
            return HttpResponse("Sorry, two password does not match")
        else:
            models.UserModel.objects.create(
                email=register_email,
                password=register_password1
            )
        return HttpResponse("Congrats, your have registered successfully")
    else:
        return render(request, "mapApp/register.html")


def reset_page(request):
    return render(request, "mapApp/reset.html")


def map_page(request):
    return render(request, "mapApp/map.html")

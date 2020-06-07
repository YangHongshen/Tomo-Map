from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


# Create your models here.
class FriendList(models.Model):
    username = models.CharField(max_length=150)
    friend = models.CharField(blank=True, default="", max_length=150)
    friend_request_received = models.CharField(blank=True, default="", max_length=150)
    friend_request_sent = models.CharField(blank=True, default="", max_length=150)

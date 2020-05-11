from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


# Create your models here.

class UserModel(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.email

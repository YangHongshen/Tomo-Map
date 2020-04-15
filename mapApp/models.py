from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)

    def validate_email(self):
        email_validator = EmailValidator()
        try:
            email_validator(self.email)
        except ValidationError:
            return False
        return True

    def __str__(self):
        return self.username

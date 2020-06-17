from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


# Create your models here.
class FriendList(models.Model):
    username = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)
    friend = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    friend_request_received = models.ForeignKey(User, blank=True, related_name="+", default="",
                                                on_delete=models.CASCADE)
    friend_request_sent = models.ForeignKey(User, blank=True, related_name="+", default="", on_delete=models.CASCADE)


class NotificationList(models.Model):
    notification = models.TextField(max_length=150)
    notification_sent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    notification_received = models.ForeignKey(User, on_delete=models.CASCADE)

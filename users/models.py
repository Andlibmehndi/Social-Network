from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_ip = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    is_holiday_on_signup = models.BooleanField(default=False)

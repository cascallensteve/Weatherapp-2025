from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add `related_name` to avoid conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="weather_users",  # Change this
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="weather_user_permissions",  # Change this
        blank=True
    )

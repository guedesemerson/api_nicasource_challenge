from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


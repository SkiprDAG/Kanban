from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    board = models.ManyToManyField('board.Board', blank=True)

    def __str__(self) -> str:
        return self.username

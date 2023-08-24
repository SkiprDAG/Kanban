import uuid

from django.db import models


class Board(models.Model):
    users = models.ManyToManyField('user.CustomUser')
    owner = models.ForeignKey('user.CustomUser', on_delete=models.DO_NOTHING, related_name='owner')
    # codename = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    column = models.ManyToManyField('board.Column', blank=True)

    def __str__(self) -> str:
        return self.name


class Column(models.Model):
    # codename = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    card = models.ManyToManyField('board.Task', blank=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    # codename = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    responsible = models.ForeignKey('user.CustomUser', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    title = models.TextField()

    def __str__(self) -> str:
        return self.name

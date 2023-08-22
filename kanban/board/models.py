from django.db import models


class Board(models.Model):
    codename = models.BigIntegerField()
    name = models.CharField(max_length=255)
    column = models.ManyToManyField('board.Column', blank=True)

    def __str__(self) -> str:
        return self.name


class Column(models.Model):
    codename = models.BigIntegerField()
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    card = models.ManyToManyField('board.Card', blank=True)

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
    codename = models.BigIntegerField()
    name = models.CharField(max_length=255)
    title = models.TextField()

    def __str__(self) -> str:
        return self.name

from django.shortcuts import render

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from board.models import Board, Column, Card
from board.serializers import BoardSerializer, ColumnSerializer, CardSerializer


class BoardViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class ColumnViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer


class CardViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

from django.shortcuts import render

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from board.models import Board, Column, Task
from board.serializers import BoardSerializer, ColumnSerializer, CardSerializer


class BoardViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filterset_fields = ['owner', ]


class ColumnViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def perform_create(self, serializer):
        s = serializer.save()
        board_id = self.request.data['board']
        board = Board.objects.get(id=board_id)
        board.column.add(s)


class CardViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        s = serializer.save()
        column_id = self.request.data['column']
        column = Column.objects.get(id=column_id)
        column.card.add(s)

from django.shortcuts import render

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from board.models import Board, Column, Task
from board.serializers import BoardSerializer, ColumnSerializer, TaskSerializer


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
        board_id = self.request.POST.get('board')
        board = Board.objects.get(id=board_id)
        board.column.add(s)


class CardViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer: TaskSerializer):
        obj = self.queryset[0]
        if column_id := self.request.data.get('column_id'):
            obj.column_set.clear()
            obj.column_set.add(column_id)
        serializer.save()

    def perform_create(self, serializer):
        s = serializer.save()
        column_id = self.request.POST.get('column')
        column = Column.objects.get(id=column_id)
        column.card.add(s)

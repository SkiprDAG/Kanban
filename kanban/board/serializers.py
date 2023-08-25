from rest_framework import serializers

from board.models import Board, Column, Task


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        depth = 2


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    column_id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = "__all__"

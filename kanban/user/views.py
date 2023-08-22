from django.shortcuts import render

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from user.models import CustomUser
from user.serializers import CustomUserSerializer


class CustomUserViewSet(mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


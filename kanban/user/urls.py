from django.urls import path, include

from rest_framework import routers

from user.views import CustomUserViewSet


router = routers.SimpleRouter()
router.register(r'users/board', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

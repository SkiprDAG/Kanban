from django.urls import path, include

from rest_framework import routers

from board.views import BoardViewSet, ColumnViewSet, CardViewSet


router = routers.SimpleRouter()
router.register(r'board', BoardViewSet)
router.register(r'column', ColumnViewSet)
router.register(r'task', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
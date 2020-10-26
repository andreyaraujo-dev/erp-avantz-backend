from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .viewset import RotinasViewSet

router = SimpleRouter()
router.register(r'routines', RotinasViewSet, basename='permissions')

urlpatterns = router.urls

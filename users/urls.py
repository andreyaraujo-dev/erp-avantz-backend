from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import profile, login, register
from .viewset import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
# router.register(r'users/set_password',
#                 UserViewSet.set_password, basename='set_password')

urlpatterns = [
    path('profile', profile, name='profile'),
    path('login', login, name='login'),
    path('register', register, name='register'),
]

urlpatterns += router.urls

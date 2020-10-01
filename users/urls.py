from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import profile, login, register
from .viewset import UsersViewset

router = DefaultRouter()
router.register(r'users', UsersViewset, basename='users')

urlpatterns = [
    path('profile', profile, name='profile'),
    path('login', login, name='login'),
    path('register', register, name='register'),
]

urlpatterns += router.urls

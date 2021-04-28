from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all'),
]

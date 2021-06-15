from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_all, name='list_all'),
    path('update/', views.update, name='update_settings'),
]

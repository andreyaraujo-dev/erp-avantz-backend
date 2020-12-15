from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import list_all, filter_dropdown

urlpatterns = [
    path('list/', list_all, name='list_all_contasmv'),
    path('filter_dropdown/', filter_dropdown, name='filter_dropdown'),
]
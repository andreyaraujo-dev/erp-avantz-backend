from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all'),
    path('<str:name>', views.find_products_by_name,
         name='find_products_by_name'),
]

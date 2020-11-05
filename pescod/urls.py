from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='list_all_persons')
]

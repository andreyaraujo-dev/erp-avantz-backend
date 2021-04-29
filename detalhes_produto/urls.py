from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data_for_quick_search, name='get_data_for_quick_search')
]

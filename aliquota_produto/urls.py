from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_all, name='find_all_aliquots'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all'),
    path('<str:name>/', views.get_all, name='find_by_name'),
    path('create', views.create, name='create_institution'),
    path('details/<int:id>/', views.details, name='details_institution'),
    path('update/<int:id>/', views.update, name='update_institution'),
    path('deactivate/<int:id>/', views.deactivate,
         name='deactivate_institution'),
    path('activate/<int:id>/', views.activate, name='acvite_institution'),
]

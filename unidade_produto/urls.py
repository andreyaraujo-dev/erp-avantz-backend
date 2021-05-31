from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all'),
    path('create', views.create, name='create_unit'),
    path('update/<int:id>', views.update, name='update_unit'),
    path('delete/<int:id>', views.delete, name='delete_unit'),
    path('initials/<str:initials>',
         views.find_by_initials, name='find_by_initials'),
]

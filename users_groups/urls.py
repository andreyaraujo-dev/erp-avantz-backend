from django.urls import path, include
from .views import index, details, edit, delete, create

urlpatterns = [
    path('', index, name='list_all_groups'),
    path('register', create, name='register_group'),
    path('details/<int:id>', details, name='details_group'),
    path('edit/<int:id>', edit, name='edit_group'),
    path('delete/<int:id>', delete, name='delete_group'),
]

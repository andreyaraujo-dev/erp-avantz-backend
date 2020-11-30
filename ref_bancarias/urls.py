from django.urls import path, include
from .views import index, store, update, delete

urlpatterns = [
    path('<int:id_person>', index, name='get_all_banking_references'),
    path('create', store, name='register_banking_references'),
    path('update', update, name='update_banking_references'),
    path('delete/<int:id_reference>', delete,
         name='delete_banking_references'),
]

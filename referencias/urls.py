from django.urls import path, include
from .views import index, store, update, delete

urlpatterns = [
    path('<int:id_person>', index, name='get_all_reference'),
    path('create', store, name='register_person_reference'),
    path('update', update, name='update_person_reference'),
    path('delete/<int:id_reference>', delete, name='delte_person_reference'),
]

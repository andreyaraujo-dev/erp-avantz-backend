from django.urls import path, include
from .views import index, delete, store_person_physical

urlpatterns = [
    path('', index, name='list_all_persons'),
    path('delete/<int:id_person>', delete, name='delete_person'),
    path('physical/create', store_person_physical,
         name='create_person_physical'),
]

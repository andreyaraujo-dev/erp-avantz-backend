from django.urls import path, include
from .views import index, store, update, delete

urlpatterns = [
    path('<int:id_person>', index, name='get_all_phones'),
    path('create', store, name='register_phone'),
    path('update', update, name='update_phone'),
    path('delete/<int:id_phone>', delete, name='delte_phone'),
]

from django.urls import path, include
from .views import index, store, update, delete


urlpatterns = [
    path('<int:id_person>', index, name='get_all_adresses'),
    path('create', store, name='create_adress'),
    path('update/<int:id_adress>', update, name='update_adress'),
    path('delete/<int:id_adress>', delete, name='delete_adress'),
]

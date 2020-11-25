from django.urls import path, include
from .views import index, store

urlpatterns = [
    path('<int:id_person>', index, name='get_all_mails'),
    path('create', store, name='register_mail_user'),
]

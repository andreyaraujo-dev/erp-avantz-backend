from django.urls import path, include
from .views import index, store, update, delete

urlpatterns = [
    path('<int:id_person>', index, name='get_all_mails'),
    path('create', store, name='register_mail_user'),
    path('update', update, name='update_mail_user'),
    path('delete/<int:id_mail>', delete, name='delte_mail_user'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all_manufacturer'),
    path('create', views.create, name='create_manufacturer'),
    path('update/<int:id>', views.update, name='update_manufacturer'),
    path('delete/<int:id>', views.delete, name='delete_manufacturer'),
    path('<int:id>', views.find_by_id, name='find_by_id_manufacturer'),
    path('brand/<str:brand>', views.find_by_brand,
         name='find_by_brand_manufacturer'),
]

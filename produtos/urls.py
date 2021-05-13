from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all, name='get_all'),
    path('<str:name>', views.find_products_by_name,
         name='find_products_by_name'),
    path('details/<int:id>', views.details, name='details_product'),
    path('deactivate/<int:id>', views.deactivate, name='deactivate_product'),
    path('activate/<int:id>', views.activate, name='activate_product'),
    path('create/', views.create, name='create_product'),
    path('update/<int:id>', views.update, name='update_product'),
]

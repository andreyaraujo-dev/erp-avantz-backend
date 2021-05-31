from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>', views.find_by_product_id, name='find_product_items_by_id'),
    path('', views.find_by_matriz, name='find_items_by_matriz'),
]

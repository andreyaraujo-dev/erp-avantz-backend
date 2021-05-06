from django.urls import path, include
from .views import index, select_ufs, select_cities

urlpatterns = [
    path('', index, name='list_all_counties'),
    path('ufs', select_ufs, name='list_distinct_ufs'),
    path('cities/<int:uf_id>', select_cities, name='select_cities')
]

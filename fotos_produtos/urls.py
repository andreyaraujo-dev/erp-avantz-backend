from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:product_id>', views.upload, name='upload_foto_produto'),
    path('<int:product_id>', views.find_by_product_id,
         name='find_photo_by_product_id'),
]

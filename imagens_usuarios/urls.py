from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewset import ImagemUsuarioViewSet
from .views import get_image_perfil, upload_image

router = DefaultRouter()
router.register(r'imagem', ImagemUsuarioViewSet, basename='imagens')

urlpatterns = [
    path('list', get_image_perfil, name='imagem_perfil'),
    path('upload', upload_image, name='upload_image'),
]

urlpatterns += router.urls

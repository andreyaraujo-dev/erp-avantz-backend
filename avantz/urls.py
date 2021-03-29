"""avantz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from users import urls as users_urls
from permissions import urls as permissions_urls
from users_groups import urls as user_groups_urls
from pescod import urls as pescod_urls
from emails import urls as mails_urls
from enderecos import urls as adresses_urls
from ref_bancarias import urls as banking_ref_persons_urls
from referencias import urls as person_references_urls
from telefones import urls as telefones_urls
from bancos import urls as bancos_urls

# from permissions.viewset import RotinasViewSet
# from users_groups.viewset import UserGroupsViewSet

# router = DefaultRouter()
# router.register(r'user_permissions', RotinasViewSet)
# router.register(r'user_groups', UserGroupsViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', include(users_urls)),
    # path('imagem/', include(imagem_usuario_urls)),
    path('groups/', include(user_groups_urls)),
    path('permissions/', include(permissions_urls)),
    path('persons/', include(pescod_urls)),
    path('mails/', include(mails_urls)),
    path('addresses/', include(adresses_urls)),
    path('banking_references/', include(banking_ref_persons_urls)),
    path('persons_references/', include(person_references_urls)),
    path('phones/', include(telefones_urls)),
    path('banking/', include(bancos_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls

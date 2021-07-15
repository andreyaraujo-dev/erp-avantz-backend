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

from contasfin import urls as contasfin_urls
from contasmv import urls as contasmv_urls
from emails import urls as mails_urls
from enderecos import urls as adresses_urls
from it_ped import urls as itensped_urls
from pedidos import urls as pedidos_urls
from permissions import urls as permissions_urls
from pescod import urls as pescod_urls
from ref_bancarias import urls as banking_ref_persons_urls
from referencias import urls as person_references_urls
from telefones import urls as telefones_urls
from users import urls as users_urls
from users_groups import urls as user_groups_urls
from bancos import urls as bancos_urls
from municipios import urls as municipios_urls
from produtos import urls as produtos_urls
from unidade_produto import urls as unidades_urls
from fabricante_produto import urls as fabricante_urls
from detalhes_produto import urls as detalhes_produto_urls
from configuracoes_instituicao import urls as configuracoes_urls
from instituicao import urls as institution_urls
from produtos_itens import urls as produtos_itens_urls
from produtos_grupos import urls as produtos_grupos_urls
from fotos_produtos import urls as fotos_produtos_urls
from aliquota_produto import urls as aliquota_produto_urls
from funcionarios import urls as funcionarios_urls

# from permissions.viewset import RotinasViewSet
# from users_groups.viewset import UserGroupsViewSet

# router = DefaultRouter()
# router.register(r'user_permissions', RotinasViewSet)
# router.register(r'user_groups', UserGroupsViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('account_movement/', include(contasmv_urls)),
    path('admin/', admin.site.urls),
    path('adresses/', include(adresses_urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('banking_references/', include(banking_ref_persons_urls)),
    path('financial_accounts/', include(contasfin_urls)),
    path('groups/', include(user_groups_urls)),
    path('itenspedido/', include(itensped_urls)),
    # path('imagem/', include(imagem_usuario_urls)),
    path('mails/', include(mails_urls)),
    path('pedidos/', include(pedidos_urls)),
    path('permissions/', include(permissions_urls)),
    path('persons/', include(pescod_urls)),
    path('persons_references/', include(person_references_urls)),
    path('phones/', include(telefones_urls)),
    path('users/', include(users_urls)),
    path('addresses/', include(adresses_urls)),
    path('banking_references/', include(banking_ref_persons_urls)),
    path('persons_references/', include(person_references_urls)),
    path('phones/', include(telefones_urls)),
    path('banking/', include(bancos_urls)),
    path('counties/', include(municipios_urls)),
    path('products/', include(produtos_urls)),
    path('prod-items/', include(produtos_itens_urls)),
    path('prod-groups/', include(produtos_grupos_urls)),
    path('units/', include(unidades_urls)),
    path('fabricator/', include(fabricante_urls)),
    path('stock/', include(detalhes_produto_urls)),
    path('settings/', include(configuracoes_urls)),
    path('institution/', include(institution_urls)),
    path('photos/', include(fotos_produtos_urls)),
    path('aliquot/', include(aliquota_produto_urls)),
    path('employees/', include(funcionarios_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls

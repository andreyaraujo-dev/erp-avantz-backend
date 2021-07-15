from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all, name='listar_funcionarios'),
    path('<str:name>/', views.get_all, name='listar_funcionarios_nome'),
    path('create', views.create, name='criar_funcionario'),
    path('delete/<int:id>/', views.delete, name='deletar_funcionario'),
    path('update/<int:id>/', views.update, name='atualizar_funcionario'),
    path('change_situation/<int:id>/', views.change_situation,
         name='mudar_situacao_funcionario'),
    path('show/<int:id>/', views.show, name='detalhes_funcionario'),
]

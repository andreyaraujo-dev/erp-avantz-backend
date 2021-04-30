from rest_framework.response import Response
from rest_framework import exceptions

from .models import Instit
from .serializers import InstituicaoSerializer


def search_matriz(id):
    try:
        instituicao = Instit.objects.get(pk=id)
        instituicao_serialized = InstituicaoSerializer(instituicao).data

        matriz = Instit.objects.filter(
            id_instituicao=instituicao_serialized['idmatriz']).get()
        matriz_serialized = InstituicaoSerializer(matriz).data
        return matriz_serialized['idmatriz']
    except:
        raise exceptions.APIException('Não foi possível encontrar a matriz')

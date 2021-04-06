from rest_framework.serializers import ModelSerializer
from .models import Municipios


class MunicipiosSerializer(ModelSerializer):
    class Meta:
        model = Municipios
        fields = ['id_municipios', 'descr', 'uf_sigla', 'coduf', 'ibge']

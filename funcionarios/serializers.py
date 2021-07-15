from rest_framework.serializers import ModelSerializer
from .models import Funcio


class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcio
        fields = '__all__'

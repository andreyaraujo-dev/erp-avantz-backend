from rest_framework.serializers import ModelSerializer
from .models import Configs


class ConfiguracoesInstituticaoSerializer(ModelSerializer):
    class Meta:
        model = Configs
        fields = '__all__'

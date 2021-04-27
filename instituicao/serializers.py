from rest_framework.serializers import ModelSerializer
from .models import Instit


class InstituicaoSerializer(ModelSerializer):
    class Meta:
        model = Instit
        fields = '__all__'

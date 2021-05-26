from rest_framework.serializers import ModelSerializer
from .models import Fotos


class FotosSerializer(ModelSerializer):
    class Meta:
        model = Fotos
        fields = '__all__'

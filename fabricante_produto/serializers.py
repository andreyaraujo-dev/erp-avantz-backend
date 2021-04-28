from rest_framework.serializers import ModelSerializer
from .models import Fabpro


class FabricanteProdutoSerializer(ModelSerializer):
    class Meta:
        model = Fabpro
        fields = ['id', 'instit', 'marca', 'fabr', ]

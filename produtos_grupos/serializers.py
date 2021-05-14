from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import ProdGrp


class GrupoProdutoSerializer(ModelSerializer):
    class Meta:
        model = ProdGrp
        fields = '__all__'

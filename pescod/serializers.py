from rest_framework.serializers import ModelSerializer
from .models import Pescod


class PescodSerializer(ModelSerializer):
    class Meta:
        model = Pescod
        fields = '__all__'

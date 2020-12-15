from rest_framework import serializers
from .models import It_Ped


class ItPedSerializers(serializers.ModelSerializer):
    class Meta:
        model = It_Ped
        fields = '__all__'
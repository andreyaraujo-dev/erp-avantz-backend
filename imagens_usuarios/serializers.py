from rest_framework import serializers
from .models import ImagensUsuarios


class ImagensUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensUsuarios
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ImagensUsuariosSerializer,
                               self).to_representation(instance)
        representation['imagem'] = instance.imagem.url
        return representation

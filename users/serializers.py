from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from .models import Users


class UsersSerializers(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'foto',
                  'date_joined', 'idpescod_id', 'instit_id', 'idgrp_id', 'acess']


class ChangePasswordSerializer(serializers.Serializer):
    model = Users
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

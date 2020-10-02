from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Users


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        # User = get_user_model()
        model: Users
        fields: ['id', 'username', 'email', 'nome',
                 'login', 'idpescod_id', 'instit_id', 'idgrp_id', 'acess']

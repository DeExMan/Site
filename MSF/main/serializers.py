from rest_framework import serializers
from .models import *
from rest_framework.authtoken.views import Token


class TiltyardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiltyard
        fields = ['id', 'name', 'nomination', 'age_category', 'league', 'state', 'referee', 'stage']
        depth = 1


class TiltyardSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Tiltyard
        fields = ['id', 'name', 'nomination', 'age_category', 'league', 'state', 'referee', 'stage']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'patronymic', 
        'club', 'rating', 'number', 'scores', 'victoryPoints', 'pool', 'tiltyard', 
        'stage',]
        depth = 1

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

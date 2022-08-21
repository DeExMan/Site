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
        fields = ['id', 'email', 'password', 
        'first_name', 'last_name', 'patronymic', 
        'club', 'rating', 'number', 
        'victoryPoints', 
        'pool', 'tiltyard', 
        'stage', 'role' , 'category'
        ]
        depth = 1

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    
class UserSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['rating', 'number', 'victoryPoints', 'pool', 'tiltyard', 
        'stage', ]


class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'patronymic', 
        'club', 'rating', 'number',  'victoryPoints', 'pool', 'tiltyard', 
        'stage', 'category']
        depth = 1


class BattleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattleOrder
        fields = ['id', 'left_fighter','right_fighter', "Tiltyard", "Order", "stage", "left_scores", "right_scores", ]
        depth = 2


class BattleOrderSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BattleOrder
        fields = ['left_fighter','right_fighter', "Tiltyard", "Order", "stage", "left_scores", "right_scores" ]


class BattleOrderSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = BattleOrder
        fields = ["left_scores", "right_scores" ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'last_name': 'The username should only contain alphanumeric characters'}

    class Meta:
        model = User
        fields = ['email',  'last_name',   'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        last_name = attrs.get('last_name', '')


        if not last_name.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

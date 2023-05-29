from rest_framework import serializers
from .models import User


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
        )
        read_only_fields = [
            'id'
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Email already exists'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserAuthenticateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )



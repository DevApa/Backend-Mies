from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from entrepreneur.models import Usuario


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = Usuario
        fields = ['email', 'full_name', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        full_name = attrs.get('full_name', '')

        if not full_name.isalnum():
            raise serializers.ValidationError('El nombre únicamente puede contener caracteres alfanumerios')
        return attrs

    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)


class EmailVerifySerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = Usuario
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    names = serializers.CharField(max_length=255, min_length=6, read_only=True)
    token = serializers.CharField(max_length=255, min_length=6, read_only=True)
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)

    class Meta:
        model = Usuario
        exclude = ['create_time', 'last_login', 'is_admin', 'identify', 'password']

        read_only_fields = ['token']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user.is_active:
            raise AuthenticationFailed('Account disable, contact admin')
        if not user:
            raise AuthenticationFailed('Invalid creadencial, try again')

        return {
            'email': user.email,
            'full_name': user.full_name,
            'token': user.token
        }


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['create_time', 'last_login', 'is_admin', 'identify', 'password']


class LogoutSerializer(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = ['id']

from rest_framework import serializers

from entrepreneur.models import Usuario


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ('create_time', 'last_login', 'is_admin')

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'email': instance['email'],
            'full_name': instance['names'],
            'identify': instance['identify'],
            'password': instance['password'],
            'status': instance['status'],
            'rol': instance['rol']
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['create_time', 'last_login', 'is_admin']

    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class UserTokenSerializer(serializers.ModelSerializer):
    """
    Habilita la creación de Tokens de usuarios
    """
    class Meta:
        model = Usuario
        exclude = ('create_time', 'last_login')

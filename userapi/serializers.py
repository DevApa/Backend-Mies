from rest_framework import serializers

from entrepreneur.models import Usuario


class UserListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField()
    email = serializers.CharField(max_length=100)
    full_name = serializers.CharField(max_length=100)
    identify = serializers.CharField(max_length=10)
    status = serializers.CharField(max_length=1)
    rol = serializers.IntegerField()

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

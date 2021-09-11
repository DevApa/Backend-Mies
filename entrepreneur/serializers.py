from rest_framework import serializers

from entrepreneur.models import Entrepreneurship, Permission, Role, RolePermission, ActivityEconomic


class EntrepreneurshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entrepreneurship
        fields = '__all__'

    def create(self, validated_data):
        entrepreneurship = Entrepreneurship(**validated_data)
        entrepreneurship.save()
        return entrepreneurship

    def update(self, instance, validated_data):
        update_entrepreneurship = super().update(instance, validated_data)
        update_entrepreneurship.save()
        return update_entrepreneurship


class ActivityEconomicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityEconomic
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = '__all__'

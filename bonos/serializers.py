from rest_framework import serializers

from entrepreneur.models import Bond


class BonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = '__all__'
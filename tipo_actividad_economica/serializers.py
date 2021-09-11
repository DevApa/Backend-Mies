from rest_framework import serializers

from tipo_actividad_economica.models import TypeActivityEconomic


class TypeActivityEconomicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeActivityEconomic
        fields = '__all__'

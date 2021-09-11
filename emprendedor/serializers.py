from rest_framework import serializers

from emprendedor.models import Entrepreneur


class EmprendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = '__all__'
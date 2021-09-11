from django.db import models
from django.db.models import fields
from rest_framework import serializers
from entrepreneur.models import Observations
from rest_framework import serializers



class Observationsserializer(serializers.ModelSerializer):
    class Meta:
        model = Observations
        fields = '__all__'
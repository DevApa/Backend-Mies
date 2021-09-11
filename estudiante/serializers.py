from django.db import models
from django.db.models import fields
from rest_framework import serializers
from estudiante.models import Student

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
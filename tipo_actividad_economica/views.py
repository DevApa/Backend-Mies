from django.shortcuts import render
from tipo_actividad_economica.models import TypeActivityEconomic
from tipo_actividad_economica import serializers
from tipo_actividad_economica.serializers import TypeActivityEconomicSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CrudActividadEconomica(APIView):
    @api_view(['GET', 'POST'])
    def crud_tipo_actividad( request):
        if request.method == 'GET':
            tipo_actividad_economica = TypeActivityEconomic.objects.all()
            serializer = TypeActivityEconomicSerializer(tipo_actividad_economica, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = TypeActivityEconomicSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET','PUT','DELETE'])
    def update_tipo_actividad(request, pk):
        if request.method == 'GET':
            tipo_actividad_economica = TypeActivityEconomic.objects.get(id=pk)
            serializer = TypeActivityEconomicSerializer(tipo_actividad_economica)
            return Response(serializer.data)
        elif request.method=='PUT':
            tipo_actividad_economica = TypeActivityEconomic.objects.get(id=pk)
            serializer = TypeActivityEconomicSerializer(tipo_actividad_economica, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            tipo_actividad_economica = TypeActivityEconomic.objects.get(id=pk)
            tipo_actividad_economica.delete()
            return Response({"Mensaje": "Emprendedor eliminado"} , status=status.HTTP_204_NO_CONTENT)
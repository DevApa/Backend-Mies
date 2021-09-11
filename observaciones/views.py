from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import fields
from observaciones import serializers
from observaciones.serializers import Observationsserializer
from entrepreneur.models import Observations
from observaciones import views
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view


class Crudobsevarciones(APIView):  
    @api_view(['GET','POST'])
    def user_obsrvaciones_view(request):
        if request.method=='GET':
         Observaciones = Observations.objects.all()
         serializer = Observationsserializer(Observaciones, many=True)
         return Response(serializer.data)
        elif request.method =='POST':
         serializer=Observationsserializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    @api_view(['GET','PUT','DELETE'])
    def user_observaciones_view(request,pk=None):
        if request.method=='GET':
         Observaciones=Observations.objects.get(id=pk)
         serializer = Observationsserializer(Observaciones)
         return Response(serializer.data)
        elif request.method=='PUT':
         Observaciones=Observations.objects.get(id=pk)
         serializer=Observationsserializer(Observaciones,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        elif request.method=='DELETE':
         serializer=Observations.objects.get(id=pk)
         serializer.delete()
         return Response({"Mensaje": "bonos  eliminado"}, status=status.HTTP_204_NO_CONTENT )


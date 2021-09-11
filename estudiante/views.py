from django.shortcuts import render
from estudiante.models import Student
from estudiante.serializers import EstudianteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

class CrudEstudiantes(APIView):
    @api_view(['GET', 'POST'])
    def crud_estudiantes(request):
        if request.method == 'GET':
            estudiante = Student.objects.all()
            serializer = EstudianteSerializer(estudiante, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = EstudianteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET','PUT','DELETE'])
    def update_estudiantes(request, pk):
        if request.method == 'GET':
            estudiante = Student.objects.get(id=pk)
            serializer = EstudianteSerializer(estudiante)
            return Response(serializer.data)
        elif request.method=='PUT':
            estudiante = Student.objects.get(id=pk)
            serializer = EstudianteSerializer(estudiante, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            estudiante = Student.objects.get(id=pk)
            estudiante.delete()
            return Response({"Mensaje": "Emprendedor eliminado"} , status=status.HTTP_204_NO_CONTENT)  
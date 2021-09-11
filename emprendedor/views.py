from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from emprendedor.models import Entrepreneur
from emprendedor.serializers import EmprendedorSerializer


class CrudEmprendedores(APIView):
    @api_view(['GET', 'POST'])
    def crud_emprendedores(request):
        if request.method == 'GET':
            emprendedor = Entrepreneur.objects.filter(status='A')
            serializer = EmprendedorSerializer(emprendedor, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = EmprendedorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET','PUT','DELETE'])
    def update_emprendedores(request, pk):
        if request.method == 'GET':
            entrepreneur = Entrepreneur.objects.get(id=pk)
            serializer = EmprendedorSerializer(entrepreneur)
            return Response(serializer.data)
        elif request.method=='PUT':
            entrepreneur = Entrepreneur.objects.get(id=pk)
            serializer = EmprendedorSerializer(entrepreneur, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            entrepreneur = Entrepreneur.objects.get(id=pk)
            entrepreneur.status = 'B'
            entrepreneur.save()
            return Response({"Mensaje": "Emprendedor eliminado"} , status=status.HTTP_204_NO_CONTENT)

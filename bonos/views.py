from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from bonos.serializers import BonoSerializer
from entrepreneur.models import Bond


class Crudbonos(APIView):
    @api_view(['GET', 'POST'])
    def user_bono_view(request):

        if request.method == 'GET':
            bonos = Bond.objects.all()
            serializer = BonoSerializer(bonos, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = BonoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])
    def user_detail_view(request, pk=None):
        if request.method == 'GET':
            bonos = Bond.objects.get(id=pk)
            serializer = BonoSerializer(bonos)
            return Response(serializer.data)
        elif request.method == 'PUT':
            bonos = Bond.objects.get(id=pk)
            serializer = BonoSerializer(bonos, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            serializer = Bond.objects.get(id=pk)
            serializer.delete()
            return Response({"Mensaje": "bonos  eliminado"}, status=status.HTTP_204_NO_CONTENT)

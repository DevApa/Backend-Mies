from rest_framework import status, viewsets
from rest_framework.response import Response

from entrepreneur.serializers import EntrepreneurshipSerializer
from userapi.serializers import UserSerializer


class EntrepreneurshipViewSet(viewsets.ModelViewSet):
    serializer_class = EntrepreneurshipSerializer
    queryset = UserSerializer.Meta.model.objects.filter(status='A')

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(status='A', id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Emprendimiento creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
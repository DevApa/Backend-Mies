from rest_framework import status, viewsets
from rest_framework.response import Response

from userapi.serializers import UserSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.filter(status='A')

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(status='A')
        return self.get_serializer().Meta.model.objects.filter(status='A', id=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            user_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'message': 'Usuario actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'No éxiste un usuario con estas credenciales!'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        user = self.get_queryset().filter(id=pk).first()
        if user:
            user.status = 'I'
            user.save()
            return Response({'message': 'Usuario eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No éxiste un Usuario con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

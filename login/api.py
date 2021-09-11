from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status, authtoken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from login.serializers import LogoutSerializer
from userapi.serializers import UserTokenSerializer


class Login(ObtainAuthToken):
    """
    Permite el logeo de usuarios al sistema
    @param
    :email
    :password
    """
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if not login_serializer.is_valid():
            return Response({'error': 'Usuario o contraseña no validos!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = login_serializer.validated_data['user']
            if user.status == 'A':
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Successful login'
                    }, status=status.HTTP_201_CREATED)
                else:
                    all_session = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = token.objects.create(user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Successful login'
                    }, status=status.HTTP_201_CREATED)
                    """
                    return Response({
                        'error': 'Ya se ha iniciado sesión con este usuario.'
                    }, status=status.HTTP_409_CONFLICT)
                    """
            else:
                return Response({'error': 'No puede iniciar sesión con este usuario'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'Inicio correcto!'}, status=status.HTTP_200_OK)


class Logout(APIView):
    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        try:
            logout_serializer = self.serializer_class(data=request.data, context={'request': request})
            if logout_serializer.is_valid:
                user = request.data['id']
                token = authtoken.models.Token.objects.filter(user=int(user)).first()
                if token:
                    all_session = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    session_message = 'Sesiones de usuario eliminadas.'
                    token_message = 'Token eliminado.'
                    return Response({'token_message': token_message,
                                     'session_message': session_message},
                                    status=status.HTTP_200_OK)
                return Response({'error': 'No se ha encontrado un token para el usuario ingresado'},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No se ha encontrado token en le petición'},
                            status=status.HTTP_409_CONFLICT)



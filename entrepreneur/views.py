import entrepreneur
from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from entrepreneur.models import Entrepreneurship, Permission, Role, RolePermission, ActivityEconomic
from entrepreneur.serializers import EntrepreneurshipSerializer, PermissionSerializer, RoleSerializer, RolePermissionSerializer, ActivityEconomicSerializer
from .paginations import BasicPagination
from rest_framework import generics

class ListActivityEconomic(APIView):

    def get(self, request):

        ActivityEconomicList = ActivityEconomic.objects.filter(status='A')
        get_data = request.query_params

        if get_data:
            if 'typeActEcon' in get_data:
                ActivityEconomicList = ActivityEconomicList.filter(typeActEcon=get_data['typeActEcon'])

        serializer = ActivityEconomicSerializer(ActivityEconomicList, many=True)
        return Response(serializer.data)

        

    def post(self, request):

        serializer = ActivityEconomicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailActivityEconomic(APIView):

    def get_object(self, pk):
        try:
            return ActivityEconomic.objects.get(pk=pk)
        except ActivityEconomic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        activity_Economic = self.get_object(pk)
        serializer = ActivityEconomicSerializer(activity_Economic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        activity_Economic = self.get_object(pk)
        serializer = ActivityEconomicSerializer(activity_Economic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        activity_Economic = self.get_object(pk)
        activity_Economic.delete()
        return Response({"Mensaje": "Actividad economica eliminada"}, status=status.HTTP_204_NO_CONTENT)


class ListEntrepreneurships(APIView):
    
    pagination_class = BasicPagination
    serializer_class = EntrepreneurshipSerializer

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()

        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def get(self, request, format=None, *args, **kwargs):

        get_data = request.query_params
        entrepreneurships = Entrepreneurship.objects.all()

        if get_data:
            if 'entrepreneur' in get_data:
                entrepreneurships = entrepreneurships.filter(entrepreneur=get_data['entrepreneur'])

            if 'activity_eco' in get_data:
                entrepreneurships = entrepreneurships.filter(activity_eco=get_data['activity_eco'])

            

        page= self.paginate_queryset(entrepreneurships)

        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(entrepreneurships, many=True)

        return Response(serializer.data)

    #NO FILTERS
    # def get(self, request):
    #     entrepreneurships = Entrepreneurship.objects.filter(status='A')
    #     serializer = EntrepreneurshipSerializer(entrepreneurships, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class DetailEntrepreneurships(APIView):

    def get_object(self, pk):
        try:
            return Entrepreneurship.objects.get(pk=pk)
        except Entrepreneurship.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        entrepreneurship = self.get_object(pk)
        serializer = EntrepreneurshipSerializer(entrepreneurship)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        entrepreneurship = self.get_object(pk)
        serializer = EntrepreneurshipSerializer(entrepreneurship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        entrepreneurship = self.get_object(pk)
        entrepreneurship.status = 'B'
        entrepreneurship.save()
        return Response({"Mensaje": "Emprendimiento eliminado"}, status=status.HTTP_204_NO_CONTENT)



class EmprendimientosPorEntrepreneur(generics.ListAPIView):

    serializer_class = EntrepreneurshipSerializer

    def get_queryset(self):
        id_entrepreneur = self.request.query_params.get('emprendedor')
        if id_entrepreneur is not None:
            return Entrepreneurship.objects.filter(entrepreneur = id_entrepreneur)
        return Response({"details":"bad request"}, status=status.HTTP_400_BAD_REQUEST)



class ListPermission(APIView):
    @api_view(['GET', 'POST'])
    def ListPermisos(request):
        if request.method == 'GET':
            permission = Permission.objects.filter(status='A')
            serializer = PermissionSerializer(permission, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = PermissionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'POST', 'DELETE'])
    def actions(request, pk):
        try:
            permisos = Permission.objects.get(pk=pk)
        except Permission.DoesNotExist:
            return JsonResponse({'message': 'No existe el permiso'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            tutorial_data = JSONParser().parse(request)
            permisos_serializer = PermissionSerializer(permisos, data=tutorial_data)
            if permisos_serializer.is_valid():
                permisos_serializer.save()
                return JsonResponse(permisos_serializer.data)
            return JsonResponse(permisos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            try:
                record = Permission.objects.get(id=pk)
                record.delete()
                return Response({"Mensaje": "Permiso eliminado"}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"Mensaje": "error"}, status=status.HTTP_204_NO_CONTENT)

        if request.method == 'GET':
            permisosbusq = PermissionSerializer(permisos)
            return JsonResponse(permisosbusq.data)

    @api_view(['GET', 'PUT', 'POST', 'DELETE'])
    def actions(request, pk):
        try:
            permisos = Permission.objects.get(pk=pk)
        except Permission.DoesNotExist:
            return JsonResponse({'message': 'No existe el permiso'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            tutorial_data = JSONParser().parse(request)
            permisos_serializer = PermissionSerializer(permisos, data=tutorial_data)
            if permisos_serializer.is_valid():
                permisos_serializer.save()
                return JsonResponse(permisos_serializer.data)
            return JsonResponse(permisos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            try:
                record = Permission.objects.get(id=pk)
                record.status = 'B'
                record.save()
                return Response({"Mensaje": "Permiso eliminado"}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"Mensaje": "error"}, status=status.HTTP_204_NO_CONTENT)

        if request.method == 'GET':
            permisosbusq = PermissionSerializer(permisos)
            return JsonResponse(permisosbusq.data)


class ListRole(APIView):
    @api_view(['GET', 'POST'])
    def ListRoles(request):
        if request.method == 'GET':
            permission = Role.objects.all()
            serializer = RoleSerializer(permission, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'POST', 'DELETE'])
    def actions(request, pk):
        try:
            rol = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            return JsonResponse({'message': 'No existe el Rol'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            rol_data = JSONParser().parse(request)
            roles_serializer = RoleSerializer(rol, data=rol_data)
            if roles_serializer.is_valid():
                roles_serializer.save()
                return JsonResponse(roles_serializer.data)
            return JsonResponse(roles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            try:
                record = Role.objects.get(id=pk)
                record.delete()
                return Response({"Mensaje": "Rol eliminado"}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"Mensaje": "error"}, status=status.HTTP_204_NO_CONTENT)

        if request.method == 'GET':
            rolbusq = RoleSerializer(rol)
            return JsonResponse(rolbusq.data)


class ListRolePermission(APIView):
    @api_view(['GET', 'POST'])
    def ListRolesPermisos(request):
        if request.method == 'GET':
            rolepermission = RolePermission.objects.all()
            serializer = RolePermissionSerializer(rolepermission, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = RolePermissionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'POST', 'DELETE'])
    def actions(request, pk):
        try:
            rolpermiso = RolePermission.objects.get(pk=pk)
        except RolePermission.DoesNotExist:
            return JsonResponse({'message': 'No existe el Rol'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            rol_data = JSONParser().parse(request)
            roles_serializer = RolePermissionSerializer(rolpermiso, data=rol_data)
            if roles_serializer.is_valid():
                roles_serializer.save()
                return JsonResponse(roles_serializer.data)
            return JsonResponse(roles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            try:
                record = RolePermission.objects.get(id=pk)
                record.delete()
                return Response({"Mensaje": "Rol permiso eliminado"}, status=status.HTTP_204_NO_CONTENT)
            except:
                return Response({"Mensaje": "error"}, status=status.HTTP_204_NO_CONTENT)

        if request.method == 'GET':
            rolbusq = RolePermissionSerializer(rolpermiso)
            return JsonResponse(rolbusq.data)

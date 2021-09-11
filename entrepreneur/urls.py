from django.urls import path, re_path
from entrepreneur import views


urlpatterns = [
    path('actividad_economica/', views.ListActivityEconomic.as_view()),
    path('actividad_economica/<int:pk>/', views.DetailActivityEconomic.as_view()),
    path('emprendimientos/', views.ListEntrepreneurships.as_view()),
    path('emprendimientos/<int:pk>/', views.DetailEntrepreneurships.as_view()),
    path('permisos/', views.ListPermission.ListPermisos),
    path('rol/', views.ListRole.ListRoles),
    path('rol/permisos/', views.ListRolePermission.ListRolesPermisos),
    path('permisos/<int:pk>/', views.ListPermission.actions),
    path('rol/<int:pk>/', views.ListRole.actions),
    path('rol/permisos/<int:pk>/', views.ListRolePermission.actions),
]
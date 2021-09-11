from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tipo_actividad_economica import views

urlpatterns = [
    path('tipo_actividad_economica/', views.CrudActividadEconomica.crud_tipo_actividad),
    path('tipo_actividad_economica/<int:pk>/',views.CrudActividadEconomica.update_tipo_actividad),
]
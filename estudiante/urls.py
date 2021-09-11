from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from estudiante import views

urlpatterns = [
    path('estudiante/', views.CrudEstudiantes.crud_estudiantes),
    path('estudiante/<int:pk>/',views.CrudEstudiantes.update_estudiantes),
]
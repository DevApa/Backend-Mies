from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from emprendedor import views

urlpatterns = [
    path('emprendedor/', views.CrudEmprendedores.crud_emprendedores),
    path('emprendedor/<int:pk>/',views.CrudEmprendedores.update_emprendedores),
]
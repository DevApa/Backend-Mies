from django.urls import path
from observaciones import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
   path('observaciones/',views.Crudobsevarciones.user_obsrvaciones_view),
   path('observaciones/<int:pk>', views.Crudobsevarciones.user_observaciones_view),
]

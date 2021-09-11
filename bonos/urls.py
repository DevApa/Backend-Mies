
from django.urls import path
from bonos import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
   path('bonos/', views.Crudbonos.user_bono_view),
   path('bonos/<int:pk>/', views.Crudbonos.user_detail_view),


]

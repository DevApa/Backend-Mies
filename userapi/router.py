from rest_framework.routers import DefaultRouter

from userapi.api import UsuarioViewSet

router = DefaultRouter()

router.register('mies/usuario', UsuarioViewSet, basename='usuario')

urlpatterns = router.urls
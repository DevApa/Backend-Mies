from rest_framework.routers import DefaultRouter

from .api import EntrepreneurshipViewSet

router = DefaultRouter()

router.register('emprendimiento', EntrepreneurshipViewSet, basename='emprendimiento')

urlpatterns = router.urls

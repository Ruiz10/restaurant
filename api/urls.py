from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, MesaViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'mesas', MesaViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

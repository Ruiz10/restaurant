from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Mesa, Reserva
from .serializers import ClienteSerializer, MesaSerializer, ReservaSerializer
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

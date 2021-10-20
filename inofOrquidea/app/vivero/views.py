from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated, #si esta autenticado
    IsAdminUser, #si es admin
    AllowAny, #cualquier usuario
)

from . import serializer
from . import models

# Create your views here.
class ViveroViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializer.ViveroSerializer
    queryset = models.Vivero.objects.all()
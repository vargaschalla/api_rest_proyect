from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated, #si esta autenticado
    IsAdminUser, #si es admin
    AllowAny, #cualquier usuario
)

from . import serializer
from . import models


class OrquideaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializer.OrquideaSerializer
    queryset = models.Orquidea.objects.all()
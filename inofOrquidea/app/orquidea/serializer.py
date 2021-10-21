from rest_framework import serializers

from . import models


class OrquideaSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Orquidea
        fields = ('__all__')
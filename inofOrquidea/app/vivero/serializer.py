from rest_framework import serializers

from . import models


class ViveroSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Vivero
        fields = ('__all__')
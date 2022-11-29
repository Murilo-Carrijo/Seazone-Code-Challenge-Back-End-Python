"""
Serializers para APIs dos Imóveis
"""
from rest_framework import serializers

from core.models import Properties

class PropertiesSerializer(serializers.ModelSerializer):
    """Serializers para imóveis."""

    class Meta:
        model = Properties
        fields = '__all__'
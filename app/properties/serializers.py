"""
Serializers para APIs dos Imóveis
"""
from rest_framework import serializers

from core.models import (
    Properties,
    Advertisement,
)


class PropertiesSerializer(serializers.ModelSerializer):
    """Serializers para imóveis."""

    class Meta:
        model = Properties
        fields = '__all__'


class PropertyDetailSerializer(serializers.ModelSerializer):
    """Serializers para detalhe dos imóveis."""

    class Meta:
        model = Properties
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializers para os anúncios."""

    class Meta:
        model = Advertisement
        fields = '__all__'

"""
Views para as APIs de Imóveis
"""
from rest_framework import viewsets

from core.models import (
    Properties,
    Advertisement
)
from .serializers import (
    PropertiesSerializer,
    PropertyDetailSerializer,
    AdvertisementSerializer,
)


class PropertiesViewSet(viewsets.ModelViewSet):
    """View para gerenciar as APIs de Imóveis"""
    queryset = Properties.objects.all().order_by('-id')
    serializer_class = PropertyDetailSerializer

    def get_serializer_class(self):
        """Retorna a classe serializer via request."""
        if self.action == 'list':
            return PropertiesSerializer

        return self.serializer_class


class AdvertisementViewSet(viewsets.ModelViewSet):
    """View para gerenciar as APIs de anúncios."""
    queryset = Advertisement.objects.all().order_by('-id')
    serializer_class = AdvertisementSerializer

    def get_serializer_class(self):
        """Retorna a classe serializer via request."""
        if self.action == 'list':
            return AdvertisementSerializer

        return self.serializer_class

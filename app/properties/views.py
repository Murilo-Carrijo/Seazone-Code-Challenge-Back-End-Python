"""
Views para as APIs de Imóveis
"""
from rest_framework import viewsets

from core.models import Properties
from .serializers import PropertiesSerializer


class PropertiesViewSet(viewsets.ModelViewSet):
    """View para gerenciar as APIs de Imóveis"""
    queryset = Properties.objects.all().order_by('-id')
    serializer_class = PropertiesSerializer

"""
Testes para as APIs referente aos Imóveis
"""

from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Properties

from properties.serializers import PropertiesSerializer

def create_properties(**params):
    """Criar e retornar o imóvel"""
    defaults = {
        'title': 'Imóvel 1',
        'max_people': 5,
        'qty_bathrooms': 2,
        'pet_frendly': True,
        'cleaning_value': Decimal('50.50'),
    }
    defaults.update(params)

    new_property = Properties.objects.create(**defaults)
    return new_property

class PropetiesAPITest(TestCase):
    """Teste dos requests da API"""

    def test_retrive_propties(self):
        """Testando a requisição da lista de imóveis."""
        create_properties()
        create_properties()

        res = self.client.get(RECIPES_URL)

        properties_list = Properties.objects.all().order_by('-id')
        serializer = PropertiesSerializer(properties_list, many=True)
        self.assertEqual(res.status_code, serializer.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
